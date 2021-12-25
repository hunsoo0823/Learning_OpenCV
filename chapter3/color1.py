import sys
import numpy as np
import cv2

# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
planes = cv2.split(src_hsv)

# 컬러 영상 속성 확인
print('src.sahpe:', src.shape)
print('src.dtype:', src.dtype)

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])

cv2.waitKey()

cv2.destroyAllWindows()