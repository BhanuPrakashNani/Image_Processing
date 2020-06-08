import cv2
import imutils
import numpy as np
from sklearn.metrics import pairwise

class VideoCamera(object):
    def __init__(self):  
        self.video = cv2.VideoCapture(0)       
        self.num_frames = 0
        self.bg = None
        
    def __del__(self):
        self.video.release()

    def get_frame(self):
        try:
            accumWeight = 0.5
            calibrated = False
            top, right, bottom, left = 10, 350, 225, 590
            grabbed, frame = self.video.read()
            frame = imutils.resize(frame, height=530)
            frame = cv2.flip(frame, 1)
            clone = frame.copy()
            thresholded = np.zeros((265,295, 3), np.uint8)
            number = np.zeros((265,295, 3), np.uint8)
            (height, width) = frame.shape[:2]
            roi = frame[top:bottom, right:left]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)

            if self.num_frames < 30:
                
                self.run_avg(gray, accumWeight)
                if self.num_frames == 1:
                    print("[STATUS] please wait! calibrating...")
                elif self.num_frames == 29:
                    print("[STATUS] calibration successfull...")
                self.num_frames += 1
            else:

                hand = self.segment(gray)
                if hand is not None:
                    (thresholded, segmented) = hand
                    cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                    fingers = self.count(thresholded, segmented)
                    thresholded = imutils.resize(thresholded, height=265)
                    thresholded = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)
                    cv2.putText(number, str(fingers), (125,150), cv2.FONT_HERSHEY_DUPLEX, 3, (255,255,255), 2)

            cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)
            
            vertical_concat = np.concatenate((thresholded, number), axis=0)
            final = np.concatenate((clone, vertical_concat), axis=1)
        except:
            final = np.zeros((530,1001, 3), np.uint8)

        ret, jpeg = cv2.imencode('.jpg', final)
        return jpeg.tobytes()

    def run_avg(self,image, accumWeight):
    
        if self.bg is None:
            self.bg = image.copy().astype("float")
            
        cv2.accumulateWeighted(image, self.bg, accumWeight)
        
    def segment(self,image, threshold=25):
        
        diff = cv2.absdiff(self.bg.astype("uint8"), image)

        thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]
        cnts,_ = cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(cnts) == 0:
            return
        else:
            segmented = max(cnts, key=cv2.contourArea)
            return (thresholded, segmented)

    def count(self, thresholded, segmented):

        chull = cv2.convexHull(segmented)
        extreme_top    = tuple(chull[chull[:, :, 1].argmin()][0])
        extreme_bottom = tuple(chull[chull[:, :, 1].argmax()][0])
        extreme_left   = tuple(chull[chull[:, :, 0].argmin()][0])
        extreme_right  = tuple(chull[chull[:, :, 0].argmax()][0])
        cX = int((extreme_left[0] + extreme_right[0]) / 2)
        cY = int((extreme_top[1] + extreme_bottom[1]) / 2)

        distance = pairwise.euclidean_distances([(cX, cY)], Y=[extreme_left, extreme_right, extreme_top, extreme_bottom])[0]
        maximum_distance = distance[distance.argmax()]
        radius = int(0.8 * maximum_distance)
        circumference = (2 * np.pi * radius)
        circular_roi = np.zeros(thresholded.shape[:2], dtype="uint8")    
        cv2.circle(circular_roi, (cX, cY), radius, 255, 1)
        circular_roi = cv2.bitwise_and(thresholded, thresholded, mask=circular_roi)
        cnts,_ = cv2.findContours(circular_roi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        count = 0

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            
            if ((cY + (cY * 0.25)) > (y + h)) and ((circumference * 0.25) > c.shape[0]):
                count += 1

        return count