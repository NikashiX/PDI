import cv2
import sys
import numpy as np
img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,200,100,apertureSize = 5)
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,int(sys.argv[2]),int(sys.argv[3]))
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imwrite(sys.argv[4],img)