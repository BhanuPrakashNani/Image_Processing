import cv2 
import numpy as np

img = cv2.imread('7.jpg',0)
kernel = np.ones((5,5), np.uint8)
kernel2 = np.ones((2,2), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel2, iterations=1) 
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_dilation2 = cv2.dilate(img, kernel, iterations=1) 
img_erosion2 = cv2.erode(img_dilation2, kernel, iterations=1)

cv2.imshow('Input', img) 
# cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
cv2.imshow('Dilation + Erosion', img_erosion2) 
cv2.imshow('Processed 2', img_dilation + img_closing - img_erosion + img_opening) 
cv2.imshow('Processed 1', img_closing - img_erosion + img_opening)
 
cv2.imwrite('Dilation.png', img_dilation) 
cv2.imwrite('Dilation + Erosion.png', img_erosion2) 
cv2.imwrite('Processed 2.png', img_dilation + img_closing - img_erosion + img_opening) 
cv2.imwrite('Processed 1.png', img_closing - img_erosion + img_opening) 

cv2.waitKey(0)
cv2.destroyAllWindows()