import cv2
import numpy as np
img = cv2.imread('Imagewrite.png')
cv2.imshow("Orignal",img)
cv2.waitKey(0)
B,G,R = cv2.split(img)
zero = np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow("RED",cv2.merge([zero,zero,R]))
cv2.waitKey(0)
cv2.imshow("BLUE",cv2.merge([B,zero,zero]))
cv2.waitKey(0)
cv2.imshow("GREEN",cv2.merge([zero,G,zero]))
cv2.waitKey(0)
cv2.destroyAllWindows()