# resizing
import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'dogs.jpg'))

resized_img = cv2.resize(img, (640, 480))

#Otra forma de hacer "resizing":
#scale_percent = 6  # Porcentaje del tamaño original (ajusta según necesites)
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
#img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)