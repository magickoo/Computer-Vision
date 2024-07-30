# import OpenCV
import cv2

# import Numpy
import numpy as np

# read an image using imread
img = cv2.imread('dog.jpg', 0)

# creating a Histogram Equalization
# of the image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# resize the output image
scale_percent = 50 # percent of original size
width = int(res.shape[1] * scale_percent / 100)
height = int(res.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(res, dim, interpolation=cv2.INTER_AREA)

# show image input vs output
cv2.imshow('image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
