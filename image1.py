import os

import cv2

# charger l'image brut
img = cv2.imread(os.path.join('.', 'data','oiseau.jpeg'))
#reduire la taille de l'image
img_resized = cv2.resize(img, (200,200), (50, 350))
#convertir l'image en gris
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#flouter l'image
img_blur = cv2.blur(img, (30,30))
#seuiller l'image (noir et blanc)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
#redimensionner l'image
image_cropped = img[100:400 , 50:550 ]
#detecter les contours
img_edge_detection = cv2.Canny(thresh, 100, 400)






cv2.imshow('img', img)
print(img.shape)
#cv2.imshow('img_resized', img_resized)
#cv2.imshow('img_gray', img_gray)
cv2.imshow('img_edge_detection',img_edge_detection)
cv2.waitKey(0)