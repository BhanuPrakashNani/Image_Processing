import cv2
import numpy as np

img = cv2.imread('16.jpg',0)
kernel = np.ones((5,5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Input', img) 
cv2.imshow('Outline', gradient) 

cv2.imwrite('Outline.png', gradient) 

cv2.waitKey(0)
cv2.destroyAllWindows()