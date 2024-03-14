import cv2

# lire la webcam

webcam = cv2.VideoCapture(0)

# visualiser la webcam
while (True):

    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

