#Es una aplicación que permite detectar sin utilizar GPU.
#Fuente: https://github.com/computervisioneng/color-detection-opencv/blob/master/main.py
import cv2
from PIL import Image

from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow) #Me devuelve el rango de colores de "amarillos"

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) #Es una máscara que contiene para todos los píxeles que contienen el color deseado

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()