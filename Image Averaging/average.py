Open Lab: Digital Image ProcessingCSE S6
Due Jan 4, 11:59 PM
Basics with images
100 points
Ram Kumar Dec 9, 2019 (Edited Dec 20, 2019)
2019-12-09.pdf
PDF
resources.txt
Text
Your work
Turned in
lab2.py
Text
Private comments
5 class comments
mummaneni prabhathJan 8
sir,
 you said you will change the due date of  assignment
Ram KumarJan 8
Well I did change once to Dec 9. Most of them have completed. 

Not going to postpone again.
mummaneni prabhathJan 8
Last class you said you will give time for two more days,  for rotation of image question
.
Ram KumarJan 8
You can still upload despite the deadline.
mummaneni prabhathJan 9
ok sir.

import numpy as np
import argparse as ap
import cv2
import glob
import warnings
import imutils
from math import cos, sin

# a = list(map(int,input().split()))
# arr = np.array(a)
# arr2 = np.uint8(arr)
# print(arr)

# img = cv2.imread("ff_disney5_f.jpg")
# print(img[0][0])

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray)

# cv2.imshow('Greyscale image', img_gray)
# cv2.waitKey(0)

# images = [cv2.imread(file) for file in glob.glob("/panda_images/*.jpg")]

# with warnings.catch_warnings():
#     warnings.simplefilter("ignore", category=RuntimeWarning)
#     foo = np.nanmean(images, axis=0)

# images = []
# for img in glob.glob("panda_images/*.jpg"):
#     n = cv2.imread(img)
#     images.append(n)

# images = [cv2.imread(file)/26 for file in glob.glob('./panda_images/*.jpg')]
# for i in range(len(images)):
#     print(images[i][0][0])

# avg = cv2.add(images[0], images[1])//1
# for i in range(2,26):
#     avg = cv2.add(avg, images[i])//1

# cv2.imshow('Average image', avg)
# cv2.waitKey(0)

# image = np.zeros((576, 1024), dtype=np.float64)
# for file in glob.glob("./panda_images/*.jpg"):
#     img = cv2.imread(file)
#     gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)/26
#     # print(gimg.dtype)
#     image = cv2.add(image, gimg)

# image = image.astype(np.uint8)
# # print(image)
# # cv2.imshow("", image)
# # cv2.waitKey()

image = cv2.imread("./panda_images/panda01.jpg")
t=image.flatten()
arr=[]
for i in range(576):
	for j in range(1024):
		arr.append([i,j])
arr = np.array(arr)
c,s = cos(45),sin(45)
m = [[c,-s],[s,c]]
f = arr.dot(np.array(m))
f = f.astype(int)
k = np.zeros((1200, 1200), dtype=np.uint32)
for i,j in zip(f,t):
	k[i[0],i[1]+600]=j
k = k.astype(np.uint8)
cv2.imshow("", k)
cv2.waitKey()

lab2.py
Page 1 of 1