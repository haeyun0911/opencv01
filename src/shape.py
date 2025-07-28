import cv2
import numpy as np

space = np.zeros((500,1000),dtype=np.uint8)
line_color = 255
color = 255
space = cv2.line(space, (100,100), (800,400), line_color,3,1)
space = cv2.circle(space,(600,200),100,color,4,1)
space = cv2.rectangle(space, (500,200),(800,400),color,5,1)
space = cv2.ellipse(space,(500,300),(300,200),0,45,250,color,4)


cv2.imshow('line',space)

cv2.waitKey(0)
cv2.destroyAllwindow()