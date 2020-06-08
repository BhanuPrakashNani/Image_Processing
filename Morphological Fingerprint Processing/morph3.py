import cv2
import numpy as np

img = cv2.imread('11.jpg',0)
img2 = cv2.imread('9-p.jpg',0)
kernel = np.ones((5,5), np.uint8)
kernel2 = np.ones((7,7), np.uint8)
kernel3 = np.array((
	[0, 1, 0],
	[1, 1, 1],
	[0, 1, 0]),dtype='uint8')

img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_erosion = cv2.erode(img, kernel3, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel3, iterations=1)
img_opening3 = cv2.morphologyEx(img_dilation, cv2.MORPH_OPEN, kernel2)
img_closing2 = cv2.morphologyEx(img_dilation, cv2.MORPH_CLOSE, kernel)
img_opening2 = cv2.morphologyEx(img_closing2, cv2.MORPH_OPEN, kernel3)


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Input', img) 
cv2.imshow('Opening', img_opening)
cv2.imshow('Closing', img_closing)
cv2.imshow('Erosion Plus Dilation', img_dilation)
cv2.imshow('Erode + Dilate + Close',img_closing2)
cv2.imshow('Processed',img_closing2)
cv2.imshow('Final-Comparision Image', img2) 
cv2.imshow('Improved', close) 


cv2.imwrite('Input.png', img) 
cv2.imwrite('Opening.png', img_opening)
cv2.imwrite('Closing.png', img_closing)
cv2.imwrite('ErosionPlusDilation.png', img_dilation)
cv2.imwrite('ErodeDilateClose.png',img_closing2)
cv2.imwrite('Processed.png',img_closing2)
cv2.imwrite('Final-ComparisionImage.png', img2) 
cv2.imwrite('Improved.png', close) 

cv2.waitKey(0)
cv2.destroyAllWindows()