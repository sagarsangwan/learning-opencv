import cv2



image = cv2.imread("image-loading-reading/image1.jpg", 0)
# dimenstion = image.ndim
# shape = image.shape
# print(type(image))
print(image)
# print(dimenstion)
# print(shape)
cv2.imshow("city", image)
cv2.waitKey(0)
cv2.destroyAllWindows(1)