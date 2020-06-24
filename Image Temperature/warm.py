#Code Resource - http://www.askaswiss.com/2016/02/how-to-manipulate-color-temperature-opencv-python.html

import cv2
import numpy as np
import collections
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

def create_LUT_8UC1(x, y):
    spl = UnivariateSpline(x, y)
    return spl(range(256))

incr_ch_lut = create_LUT_8UC1([0, 64, 128, 192, 256],[0, 70, 140, 210, 256])
decr_ch_lut = create_LUT_8UC1([0, 64, 128, 192, 256],[0, 30, 80, 120, 192])

img_bgr_in = cv2.imread("hist.png")
 
c_b, c_g, c_r = cv2.split(img_bgr_in)
c_r = cv2.LUT(c_r, incr_ch_lut).astype(np.uint8)
c_b = cv2.LUT(c_b, decr_ch_lut).astype(np.uint8)
img_bgr_warm = cv2.merge((c_b, c_g, c_r))
c_b = cv2.LUT(c_b, decr_ch_lut).astype(np.uint8)
 
c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_bgr_warm,cv2.COLOR_BGR2HSV))
c_s = cv2.LUT(c_s, incr_ch_lut).astype(np.uint8)
 
img_bgr_warm = cv2.cvtColor(cv2.merge((c_h, c_s, c_v)),cv2.COLOR_HSV2BGR)

cv2.imshow("ajskd",img_bgr_warm)
cv2.waitKey(0)
