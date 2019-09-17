import cv2
img = cv2.imread('IMG_20171018_134443.jpg')
resize = cv2.resize(img,(480,520),interpolation = cv2.INTER_AREA)
cv2.imshow('Output Image',resize)
key = cv2.waitKey(0)& 0xFF
if(key == 27):#27 is the ascii code of erase
    cv2.destroyAllWindows()
elif key == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('Imagewrite.png',resize)#change the name and extention of the image
    cv2.destroyAllWindows()
