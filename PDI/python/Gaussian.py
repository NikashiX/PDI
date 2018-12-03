import cv2
import sys
kernel = (int(sys.argv[2]),int(sys.argv[3]))
img = cv2.imread(sys.argv[1])
blur = cv2.GaussianBlur(img,kernel,0)
cv2.imwrite(sys.argv[4],blur)
