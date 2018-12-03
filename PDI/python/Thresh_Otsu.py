import cv2
import sys

img = cv2.imread(sys.argv[1])
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2 = cv2.threshold(grayscaled,sys.argv[2], sys.argv[3],cv2.THRESH_OTSU)
cv2.imwrite(sys.argv[4],threshold2)