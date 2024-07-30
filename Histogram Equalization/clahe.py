import cv2
import numpy as np

image = cv2.imread("handnotes.jpg")

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))

# Converting the image to grayscale
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=5)
final_img = clahe.apply(image_bw) + 30

# Ordinary thresholding the same image
_, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)

# Resizing the output images for better display
scale_percent = 70  # percent of original size
width = int(ordinary_img.shape[1] * scale_percent / 100)
height = int(ordinary_img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize images
resized_ordinary_img = cv2.resize(ordinary_img, dim, interpolation=cv2.INTER_AREA)
resized_final_img = cv2.resize(final_img, dim, interpolation=cv2.INTER_AREA)

# Showing the two images
cv2.imshow("Ordinary Threshold", resized_ordinary_img)
cv2.imshow("CLAHE Image", resized_final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
