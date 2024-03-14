import os
import cv2



# img = cv2.imread(os.path.join('.', 'data', 'freelancer.png'))

# example with removing noise (image pour exemple pas pertinente)
img = cv2.imread(os.path.join('.', 'data', 'image_bruit.jpeg'))
k_size = 21
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 10)
img_mediam_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_mediam_blur', img_mediam_blur)


print(img.shape)
cv2.waitKey(0)