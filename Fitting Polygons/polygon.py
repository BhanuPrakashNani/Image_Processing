import cv2 
import numpy as np

count=0
img = cv2.imread('polygons.jpg', cv2.IMREAD_GRAYSCALE)  
cv2.imshow('gray', img)
cv2.waitKey(0)

_,threshold = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY) 
cv2.imshow('Threshold Image', threshold)
cv2.imwrite('Threshold.jpg', threshold)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', img)
cv2.imwrite('Contours.jpg', img)
cv2.waitKey(0)

image2 = cv2.imread('polygons.jpg')
for contour in contours:
	peri = cv2.arcLength(contour, True)
	approx = cv2.approxPolyDP(contour,0.05 * cv2.arcLength(contour, True), True)
	if len(approx) == 3	:
		cv2.drawContours(image2, contour, -1, (0, 0, 0), 3)
		count = count + 1

print("Number of Triangles in the image: " + str(count)) 
cv2.imshow('Triangles Detected', image2)
cv2.imwrite('Triangles.jpg', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()	