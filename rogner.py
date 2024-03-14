# crop an image

import os
import cv2


# charger l'image
img= cv2.imread(os.path.join('.', 'data', 'chien.jpeg'))

print(img.shape)

cropped_img = img[0:388, 250:625]
print(cropped_img.shape)
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)