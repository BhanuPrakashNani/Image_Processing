import cv2
import numpy as np

def piecewise(img,h,w):
	for i in range(h):
		for j in range(w):
			if(img[i][j] > 105 and img[i][j] < 165):
				img[i][j] =10


img = cv2.imread('1.jpg', 0)
(h,w) = img.shape[:2]

piecewise(img,h,w)

cv2.imshow("image",img)
cv2.imwrite("image.jpg", img)
cv2.waitKey(0)