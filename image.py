#Importer librairies
import os
import cv2

#Charger l'image
image_path = os.path.join('.', 'data', 'oiseau.jpeg')
image = cv2.imread(image_path)

#Enregistrer l'image
cv2.imwrite(os.path.join('.', 'data', 'oiseau_loaded.jpeg'), image)

#Afficher l'image
cv2.imshow("image", image)
cv2.waitKey(0)