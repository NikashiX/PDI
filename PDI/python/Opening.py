import cv2
import sys
kernel = (int(sys.argv[2]),int(sys.argv[3]))
img = cv2.imread(sys.argv[1])
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite(sys.argv[4],opening)
