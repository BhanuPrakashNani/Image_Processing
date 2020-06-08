import cv2 
import numpy as np 

image = cv2.imread('bubblingFish.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

edged = cv2.Canny(gray, 30, 200) 
cv2.waitKey(0) 
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.imwrite('CannyFish.jpg', edged)  
cv2.waitKey(0) 

print("Number of Contours: " + str(len(contours))) 
  
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
  
cv2.imshow('Contours', image)
cv2.imwrite('Contours.jpg', image) 
cv2.waitKey(0) 

image2 = cv2.imread('bubblingFish.jpg')
if len(contours) != 0:
	c = max(contours, key = cv2.contourArea)
cv2.drawContours(image2, c, -1, (0, 255, 0), 3)
cv2.imshow('Largest Contour', image2)
cv2.imwrite('LargestContour.jpg', image2) 
cv2.waitKey(0) 

cv2.destroyAllWindows() 