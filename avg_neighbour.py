import cv2
from padding import *

img2 = image.copy()

for i in range(2,258):
    for j in range(2,258):
        
        vector_sum = 0
        n = 0
        
        for k in range(i-2,i+3):
            for l in range(j-2,j+3):
                
                n += 1
                vector_sum += image[k,l].astype(int)
                
        vector_mean = (vector_sum - image[i,j]) / (n-1)
        img2[i,j] = vector_mean
        
cv2.imwrite('avaerage_neighbor_operation.jpeg', img2)
cv2.imshow("Average Neighbor operation",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()