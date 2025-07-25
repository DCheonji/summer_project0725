import cv2

# 비디오를 열어서 첫번째 이미지만 저장한다.
cap = cv2.VideoCapture("test_video1.mp4")
if cap.isOpened():
  ret, img = cap.read()
  cv2.imwrite("test1.jpg", img)

cap.release()
