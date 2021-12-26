import cv2, time
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    check, frame = video.read()
    print(check)
    print(frame)
    cv2.imshow("image", frame)
    key = cv2.waitKey(10)
    if key == ord("s"):
        break

video.release()
cv2.destroyAllWindows()