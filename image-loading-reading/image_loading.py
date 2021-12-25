import cv2



image = cv2.imread("image-loading-reading/image1.jpg", 0)
dimenstion = image.ndim
shape = image.shape
print(image)
resized_image = cv2.resize(image, (500, 500))
cv2.imshow("city", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
