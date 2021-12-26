import cv2



image = cv2.imread("image-loading-reading/image1.jpg", 0)
dimenstion = image.ndim
shape = image.shape
print(shape)
resized_image = cv2.resize(image, (int(shape[1]/4), int(shape[0]/4)))
cv2.imshow("city", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(resized_image.shape)
cv2.imwrite("image-loading-reading/resized_image1.jpg", resized_image)
