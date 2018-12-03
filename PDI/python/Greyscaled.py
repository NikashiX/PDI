import cv2
import sys

img = cv2.imread(sys.argv[1])
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite(sys.argv[2],grayscaled)