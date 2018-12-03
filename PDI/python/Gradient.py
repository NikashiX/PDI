import cv2
import sys
kernel = (int(sys.argv[2]),int(sys.argv[3]))
img = cv2.imread(sys.argv[1])
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite(sys.argv[4],gradient)
