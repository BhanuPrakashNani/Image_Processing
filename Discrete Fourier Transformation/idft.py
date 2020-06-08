import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('idft.jpg',0)


dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


