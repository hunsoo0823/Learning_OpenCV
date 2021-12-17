import numpy as np
import sys
import cv2

# 비디오 파일 열기
cap = cv2.VideoCapture('PETS2000.avi')
_, back = cap.read()
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0,0), 1)

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

while True:
    _, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (0,0), 1)

    diff = cv2.absdiff(back, frame)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('diff', diff)
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
