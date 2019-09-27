import cv2
import numpy as np

img = cv2.imread('Imagewrite.png')

height, width = img.shape[:2]

# Let's get the staring pixel coordinates (top left, of cropping rectangle)
start_row , start_col   = int(height*.25),int(width*.25)

# Let's get te ending pixel coordinates (bottom right)
end_row, end_col = int(height*.75) , int(width*.75)

#cropped_img = cv2.getRectSubPix(img,(end_row,end_col),(start_row,end_col))
#or

cropped_img = img[start_row:end_row,start_col:end_row]

cv2.imshow('Normal Image',img)
cv2.imshow('Cropped Image',cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
