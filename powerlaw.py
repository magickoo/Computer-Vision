import cv2
import numpy as np

image = cv2.imread('dog.jpeg')

for gamma in [0.2, 0.5, 1, 1.5, 1.8]:
    gamma_transformation = np.array(255*(image/ 255) ** gamma , dtype = 'uint8')
    
    cv2.imwrite('gamma_transformed'+ str(gamma)+'.jpeg', gamma_transformation)
    cv2.imshow('Image: ',gamma_transformation)

cv2.waitKey(0)
cv2.destroyAllWindows()