import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0) 

edges = cv2.Canny(gray,20,100,apertureSize = 3)
cv2.imshow('canny',edges)
cv2.imwrite('canny.jpg',edges)
cv2.waitKey(0)

kernel = np.ones((3,3),np.uint8)
edges = cv2.dilate(edges,kernel,iterations = 1)
cv2.imshow('dilate',edges)
cv2.imwrite('dilate.jpg', edges)
cv2.waitKey(0)

kernel = np.ones((5,5),np.uint8)
edges = cv2.erode(edges,kernel,iterations = 1)
cv2.imshow('erode',edges)
cv2.imwrite('erode.jpg', edges)
cv2.waitKey(0)

lines = cv2.HoughLines(edges,1,np.pi/180,150)
print('number of Hough lines:', len(lines))


for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('hough.jpg',img)
cv2.imwrite('hough.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()