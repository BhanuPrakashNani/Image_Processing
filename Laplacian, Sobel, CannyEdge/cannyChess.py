import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ChessBoardGrad.png',0)
edges = cv2.Canny(img,100,200)

cv2.imshow('Original',img)
cv2.imshow('Edges',edges)

cv2.imwrite('CannyChess.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()