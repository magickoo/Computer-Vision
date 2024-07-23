import cv2

image = cv2.imread('dog.jpeg')
# Maximum intensity

L = image.max()
# subtract each intensity from max to obtain negative

negative = L- image
cv2.imshow('original',image)
cv2.imshow('negative',negative)
cv2.waitKey(0)
cv2.destroyAllWindows()