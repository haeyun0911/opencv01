import cv2
import numpy as np

image=cv2.imread('../img/like_lenna.png')
#new_height = 300
#new_width = 300
height, width, _ = image.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 30, 1)
result = cv2.warpAffine(image, matrix, (width,height), borderValue=200)

#dst = np.zeros((new_height, new_width, 3), dtype=np.uint8)

#image_small = cv2.resize(image, (100,100))
#image_big = cv2.resize(image, dsize=None, fx=2, fy=2)
#image_fliped = cv2.flip(image,1)

#dst = cv2.resize(image,(new_width, new_height))
#cv2.resize(image,(new_width, new_height), dst=dst)
#이미지를 보여주는 명령어
#cv2.imshow('Image Window', image)
#cv2.imshow('Image Window', dst)
#cv2.imshow('Image Window', image_small)
#cv2.imshow('Image Window', image_big)
#cv2.imshow('Image Window', image_fliped)
cv2.imshow('Image Window', result)

#print(image.shape)
#print(dst.shape)
#print(image_small.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
