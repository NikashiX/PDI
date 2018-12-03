import cv2
import sys

img = cv2.imread(sys.argv[1])
canny = cv2.Canny(img,int(sys.argv[2]),int(sys.argv[3]))
cv2.imwrite(sys.argv[4],canny)
