#Image Bluring
#Fuente para leer: https://docs.opencv.org/3.4/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html
import os

import cv2


img = cv2.imread(os.path.join('.','data', 'cow-salt-peper.png'))

#En caso dde requerir resizing:
#scale_percent = 6  # Porcentaje del tamaño original (ajusta según necesites)
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
#img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)



#es posible observar que la técnica de "bluring" permite eliminar o reducir considerablemente el "ruido" en una imagen.
cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)