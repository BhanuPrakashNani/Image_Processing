import cv2
import numpy as np

img = cv2.imread('5.jpg',0)
kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1) 
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
cv2.imshow('Opening', img_opening) 
cv2.imshow('Closing', img_closing)

cv2.imwrite('Erosion.png', img_erosion) 
cv2.imwrite('Dilation.png', img_dilation) 
cv2.imwrite('Opening.png', img_opening) 
cv2.imwrite('Closing.png', img_closing) 

cv2.waitKey(0)
cv2.destroyAllWindows()