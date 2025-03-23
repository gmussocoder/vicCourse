import os

import cv2


# read image
image_path = os.path.join('.', 'data', 'bird.jpg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

# visualize image

cv2.imshow('image', img)
cv2.waitKey(5000) #Esto es para que cuando presiono una tecla me deje de mostrar la imagen.