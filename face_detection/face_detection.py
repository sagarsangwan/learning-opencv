import cv2

face_cascade = cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml")
img = cv2.imread("face_detection/photo.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

face = face_cascade.detectMultiScale(img,
scaleFactor = 1.05,
minNeighbors = 5
)
for x, y, w, h in face:
    img1 = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 4)
# print(face)

cv2.imshow("image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()