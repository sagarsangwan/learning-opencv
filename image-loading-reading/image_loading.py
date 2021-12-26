import cv2
import glob


# image = cv2.imread("image-loading-reading/image1.jpg", 0)
# dimenstion = image.ndim
# shape = image.shape
# # print(shape)
# resized_image = cv2.resize(image, (int(shape[1]/4), int(shape[0]/4)))
# cv2.imshow("city", resized_image)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()
# # print(resized_image.shape)
# cv2.imwrite("image-loading-reading/resized_image1.jpg", resized_image)


images = glob.glob("image-loading-reading/sample_images/*.jpg")
print(images)
i = 1
for image in images:
    i = i+1
    img = cv2.imread(image, 0)
    resized = cv2.resize(img, (100, 100))
    cv2.imshow("img", resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("image-loading-reading/resized_sample_image/"+str(i)+".jpg", resized)
