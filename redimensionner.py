# resizing

import os
import cv2


img = cv2.imread(os.path.join('.', 'data', 'chien.jpeg' ))

print(img.shape)
resized_img = cv2.resize(img, (345, 194))
print(resized_img.shape)
cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)