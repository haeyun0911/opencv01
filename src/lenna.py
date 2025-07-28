import cv2
import numpy as np

image=cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image,dsize=None,fx=2,fy=2,)

cv2.rectangle(image_big,(225,148), (290,184),(0,0,255),10)
cv2.circle(image_big,(348,169),20,(255,0,0),10)
cv2.putText(image_big, "lenna",(10,20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
cv2.line(image_big, (36,441),(117,351),(0,255,0),10)
pts = np.array([[331,235],[267,272],[350,273]], dtype=np.int32)
cv2.polylines(image_big,[pts],True,(0,255,0),10)

cv2.imshow('rectangle', image_big)
cv2.waitKey(0)
cv2.destroyAllWindows()