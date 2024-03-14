# edge detection

import os
import numpy as np

import cv2

# charger l'image
img = cv2.imread(os.path.join('.', 'data', 'basket.jpeg'))

# comment fixer les constantes?: juste qu'il faut en tester plusieurs valeurs jusqu'à être satisfait du résultat
img_edge = cv2.Canny(img, 100, 200)

# des fonctions pour visualiser les contours (

# "augmenter l'épaisseur" des contours
img_edge_d = cv2.dilate(img_edge, np.ones((5,5), dtype = np.int8))

# "retrécir l'épaisseur" des contours
img_edge_e = cv2.erode(img_edge_d, np.ones((5,5), dtype = np.int8))



cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)

cv2.waitKey(0)