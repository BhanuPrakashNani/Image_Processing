import cv2  
import numpy as np  
 
image1 = cv2.imread('bg.jpg',0)  
image2 = cv2.imread('me.jpg',0)

fgbg2 = cv2.createBackgroundSubtractorMOG2();

img = cv2.subtract(image1, image2)
thresh1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,11,2)
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image3 = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

fgmask2 = fgbg2.apply(img);
cv2.imshow('Sub and Binary Threshold', thresh1) 
cv2.imshow('MOG2', fgmask2); 
cv2.imshow('Contours', image3); 

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  