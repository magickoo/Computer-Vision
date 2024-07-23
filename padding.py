import cv2

img = cv2.imread('dog.jpeg')

img2 = cv2.resize(img,(256,256))

#Make Black Border
image = cv2 .copyMakeBorder(img2,2,2,2,2,cv2.BORDER_CONSTANT,None,value = 0)

print('New dimensions',image.shape[0],'X',image.shape[1])

cv2.imshow('padded',image)
cv2.waitKey(0)
cv2.destroyAllWindows()