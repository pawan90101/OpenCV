import cv2
img = cv2.imread('Imagewrite.png',0)#method two is is option 0
cv2.imshow('Gray',img)
cv2.waitKey(0) &  0xFF
#thrus holding
ret , binary = cv2.threshold(img,32,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Image',binary)
cv2.waitKey(0) &  0xFF
cv2.destroyAllWindows()