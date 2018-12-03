import cv2
import sys

img = cv2.imread(sys.argv[1])
ret,binary=cv2.threshold(img, sys.argv[2], sys.argv[3], cv2.THRESH_BINARY)
cv2.imwrite(sys.argv[4],binary)