import cv2
import numpy as np



image = cv2.imread("image-loading-reading/image1.jpg", 0)
dimenstion = image.ndim
shape = image.shape
# print(type(image))
# print(image)
print(dimenstion)
print(shape)