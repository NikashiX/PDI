import cv2
import sys

img = cv2.imread(sys.argv[1])
blur = cv2.medianBlur(img,int(sys.argv[2]))
cv2.imwrite(sys.argv[3],blur)
