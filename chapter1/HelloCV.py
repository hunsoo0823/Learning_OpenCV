import cv2
import sys

img = cv2.imread('/Users/songhyeonsu/Documents/opencv/chapter1/cat.bmp') # imread로 영상을 불러온다.

if img is None:
    print('Imager load failed!') # 이미지가 없으면 출력
    sys.exit()

cv2.namedWindow('image', flags=cv2.WINDOW_AUTOSIZE) # OpenCV에서 지원하는 창을 생성하는 명령어
cv2.imshow('image', img) # 첫 번째는 어떤 창에 불러올 것이냐, 두 번째는 어떤 것을 불러올 것이냐
cv2.waitKey()            # 키보드입력을 누를떄까지 보여줌

cv2.destroyAllWindows() # 모든 창을 닫음

