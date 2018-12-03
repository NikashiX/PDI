import cv2
import sys
img = cv2.imread(sys.argv[1])
sobel = cv2.Sobel(img,cv2.CV_64F,sys.argv[2],sys.argv[3],ksize=5)
cv2.imwrite(sys.argv[4],sobel)

