import cv2
import sys
img = cv2.imread(sys.argv[1])
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img)
cv2.imwrite(sys.argv[2],equ)