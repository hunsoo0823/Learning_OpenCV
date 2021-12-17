import cv2
import sys
# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed')
    sys.exit()

h, w = img1.shape
print("w * h= {} x {}".format(w, h))

h, w = img2.shape[:2]
print("w * h= {} x {}".format(w, h))

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

x = 20
y = 10
p1 = img1[x, y]
print(p1)

p2 = img2[y, x]
print(p2)

'''
for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255)
'''

img1[:,:] = 0
img2[:,:] = (0,255,255)

if img1.ndim == 2:
    print('img1 is gray scale image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()