import cv2
import  numpy as np
img = cv2.imread('IMG_20171018_134443.jpg')
#store height and width of the image
height,width = img.shape[:2]
print(width)
print(height)

quarter_height,quarter_width = height/4,width/4
print(quarter_height)
print(quarter_width)
'''
trancelate matrix = |1 0 tx|
                    |0 1 ty|
'''
t = np.float32([[1.0,quarter_width],[0,1 , quarter_height]])
print(t)

#cv2.waitKey(0)
cv2.destroyAllWindows()