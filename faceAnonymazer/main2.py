import cv2

# Cargar el modelo preentrenado de DNN para detección de rostros
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")

# Iniciar la captura de la cámara
cap = cv2.VideoCapture(0)  # 0 para la cámara predeterminada (cambia el número si tienes varias cámaras)

while True:
    ret, frame = cap.read()  # Leer un cuadro de la cámara

    if not ret:
        print("Error al capturar la imagen de la cámara")
        break

    # Obtener las dimensiones de la imagen
    h, w = frame.shape[:2]

    # Redimensionar la imagen para el modelo
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)

    # Pasar la imagen por el modelo
    net.setInput(blob)
    detections = net.forward()

    # Dibujar los rectángulos alrededor de los rostros detectados
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Si la confianza es mayor al umbral
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Mostrar el cuadro con los rostros detectados
    cv2.imshow('Rostros Detectados', frame)

    # Salir del bucle si presionas la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
