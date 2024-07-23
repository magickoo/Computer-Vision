import cv2
from padding import *
import numpy as np

img2 = image.copy()

#Traverse the image portions

for i in range(2,258):
    for j in range(2,258):
        
        # for a 5*5 window sliding
        
        neighbors = []
        #fetch all neighbors for middle element of a 5*5 matrix
        
        for k in range(i-2,i+3):
            for l in range(j-2,j+3):
                
                neighbors.append(image[k,l])
                
        minimum = np.amin(neighbors,axis = 0)
        
        img2[i,j] = minimum

cv2.imwrite('minimum_neighbor_operation.jpg',img2) 
cv2.imshow('minimum_neighbor_operation.jpg',img2)       

