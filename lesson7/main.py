#"Edge Detection"
#Para tener en cuenta:
# https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html
# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
#Se puede detectar todos los edges en la imagen.

import os

import cv2
import numpy as np


img = cv2.imread(os.path.join('.', 'data','basketball-player.jpg'))

img_edge = cv2.Canny(img, 100, 200)

#La función "cv2.dilate" permite generar contornos más gruesos.
img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))

#La función "cv2.erode" permite generar lo opuesto a la función "cv2.dilate".
img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)