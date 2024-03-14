
# thresholding

import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'ourse.jpeg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# seuillage binaire
#ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)


# seuillage adaptatif
thresh = cv2.adaptiveThreshold(img_gray, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

# flouter (diminuer le bruit) avant de seuiller
# thresh = cv2.blur(thresh, (10,10))
# ret, thresh = cv2.threshold(thresh , 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)