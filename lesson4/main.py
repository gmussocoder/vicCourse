import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #la función "cv2.cvtColor" es para convertir color.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Esta información me permite detectar colores y sus espacios.

cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray) #se obtiene la información de los canales R, G y B a un único canal "Gris".
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)