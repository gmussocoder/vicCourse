#Para tener en cuenta: https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
#en "opencv" hay dos tipos de "image thresholding": "Simple Thresholding" y "Adaptive Thresholding" 
import os

import cv2


img = cv2.imread(os.path.join('.','data', 'bear.jpg'))

#Primero se convierte a escala de grises:
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Estas dos lineas es para probar lo que genera "img_gray"
#cv2.imshow('imgage_gray', img_gray)
#cv2.waitKey(0)


ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
#la línea anterior genera una imagen que tiene algo de ruido.
#Con las líneas siguientes aplico bluring y luego threshold puedo eliminarlo. Lo hago con las siguientes dos líneas:
thresh = cv2.blur(thresh, (10, 10))
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)
#la técnica de thresholding es util para "object detection".

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)