import numpy as np
import cv2

def on_level_changed(pos):
    global img

    level = pos * 32
    if level >= 255:
        level = 255
    img[:, :] = level
    cv2.imshow('image', img)
    print(pos)

img = np.zeros((640, 640), np.uint8)

cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0 , 8, on_level_changed)

cv2.waitKey()
cv2.destroyAllWindows()