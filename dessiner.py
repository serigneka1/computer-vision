# image drawing
import os
import cv2


img = cv2.imread(os.path.join('.', 'data', 'tableau_blanc.jpg'))

#line
cv2.line(img, (100,150), (300,450),( 0,255,0), 3)
#Rectangle
cv2.rectangle(img, (200, 300), (400, 450), (0,0,255), 2)
#Circle
cv2.circle(img, (500, 300), 50, (0,255, 0), 4)
#Text
cv2.putText(img, 'Salut Serigne', (500, 500), cv2.FONT_HERSHEY_SIMPLEX , 1, (255,255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
