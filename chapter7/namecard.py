import random
import numpy as np
import cv2
import sys

def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0])) # 칼럼 0 -> 칼럼 1 순으로 정렬한 인덱스를 반환

    pts = pts[idx] # 좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]
    
    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] == pts[[3, 2]]
    
    return pts

# 영상 불러오기
filename = 'namecard1.jpg'

if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()

# 출력 영상 설정
dw, dh = 720, 400
srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dst = np.zeros((dh, dw), np.uint8)

# 입력 영상 전처리
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cpy = src.copy()
for pts in contours:
    if cv2.contourArea(pts) < 1000: # 너무 작으면 무시
        continue
            
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    # 컨벡스가 아니고, 사각형이 아니면 무시
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
print(pers)
dst = cv2.warpPerspective(src, pers, (dw, dh))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()