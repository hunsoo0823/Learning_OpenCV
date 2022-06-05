import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed')
    sys.exit()

tm = cv2.TickMeter()
tm.start()

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

if classifier.empty():
    print('XML Load Failed!')
    sys.exit()

tm.stop()
print(tm.getTimeMilli())

faces = classifier.detectMultiScale(src, scaleFactor=1.2)

for (x, y, w, h) in faces:
    face_img = src[y:y+h, x:x+w]
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()

