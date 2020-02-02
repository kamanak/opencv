from cv2 import cv2
img = cv2.imread("lena.jpg",1) #this is colored imamge
im= cv2.imread("lena.jpg",0)
# print(img)
# print(im)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('lena_copy.png',im)