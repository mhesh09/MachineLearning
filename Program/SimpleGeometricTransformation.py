import numpy as np
import cv2 as cv

img1 = cv.imread('messi.jpg')


# Scaling Code which I have commented
# height, width = img1.shape[:2]
#res = cv.resize(img1,None,fx=2,fy=2, interpolation=cv.INTER_AREA)
# res = cv.resize(img1,(2*width,2*height),interpolation=cv.INTER_CUBIC)


#Transformation of Image
# rows, cols = img1.shape[:2]
# M = np.float32([[1,0,50],[0,1,15]])
# dst = cv.warpAffine(img1,M,(cols,rows))


pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)

print(pts1)


# cv.imshow("Display Image",dst)
# cv.waitKey(0)
# cv.destroyAllWindows()