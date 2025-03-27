#Cuando se trabaja con "contours" se detecta todos los bordes.
#Fuente: https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
#Esto puede servir para detectar objetos de manera simple sin usar un modelo tipo YOLO.

import os

import cv2

img = cv2.imread(os.path.join('.', 'data','birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV) # "cv2.THRESH_BINARY_INV" Es para invertir el color.

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.findContours(): Encuentra los contornos de los objetos en la imagen binaria.
# Parámetros:
#   thresh: Imagen binaria donde se buscan contornos.
#   cv2.RETR_TREE: Recupera todos los contornos y construye una jerarquía de anidamiento (si hay contornos dentro de otros).
#   cv2.CHAIN_APPROX_SIMPLE: Comprime los puntos del contorno, guardando solo los necesarios.
# Resultado:
#   contours: Lista de contornos detectados (cada contorno es una lista de puntos (x, y) que lo definen).
#   hierarchy: Información sobre la jerarquía entre contornos (cuál está dentro de cuál).

for cnt in contours:
    if cv2.contourArea(cnt) > 200: # "cv2.contourArea" detecta la cantidad de píxeles en el contorno.
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1) #esta función dibuja los bordes.

        x1, y1, w, h = cv2.boundingRect(cnt) #Devuelve un rectángulo para cada contorno detectado
            # cv2.boundingRect(cnt): Calcula un rectángulo mínimo que encierra completamente el contorno cnt.
            # Devuelve 4 valores:
            # x1: Coordenada X del punto superior izquierdo del rectángulo.
            # y1: Coordenada Y del punto superior izquierdo del rectángulo.
            # w: Ancho del rectángulo.
            # h: Alto del rectángulo.

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2) #imprime en la imagen un rectángulo que abarca cada contorno detectado.

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)