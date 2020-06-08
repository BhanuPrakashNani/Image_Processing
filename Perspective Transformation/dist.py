
# import the required library 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
  
  
# read the image 
img = cv2.imread('chDistorted.jpeg') 
  
# convert image to gray scale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# detect corners with the goodFeaturesToTrack function. 
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10) 
corners = np.int0(corners) 
  
# we iterate through each corner,  
# making a circle at each point that we think is a corner. 
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, 255, -1)

(h,w) = img.shape[:2]

pts1=np.float32([[0,0],[0,h],[w,0],[w,h]])
pts2=np.float32([(7.17803, 6.05628),(67.6975,198.332),(209.54, 50.1851),(231.604, 226.7)])

m = cv2.getPerspectiveTransform(pts2,pts1)
img = cv2.warpPerspective(img,m,(w,h))

cv2.imshow('Perspective', img)
plt.imshow(img), plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

