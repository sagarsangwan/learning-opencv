import cv2, time
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

time.sleep(5)
video.release()
cv2.destroyAllWindows()