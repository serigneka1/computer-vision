import os
import cv2


# charger l'image

img = cv2.imread(os.path.join('.', 'data', 'oiseau_rolier.webp'))

img_rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_rgb ', img_rgb )
cv2.imshow('img_gray ', img_gray )
cv2.imshow('img_hsv  ', img_hsv  )
cv2.waitKey(0)