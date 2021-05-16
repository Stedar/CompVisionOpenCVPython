
import cv2
import numpy as np
import os

img = cv2.imread('MyPic.png')
print(img.shape)

print(img.size)
print(img.dtype)

img = cv2.imread(cv2.samples.findFile("starry_night.jpg"))
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()
