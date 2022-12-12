import numpy as np
import cv2 as cv

img = cv.imread("messi.jpg")


# Accessing and Modifying pixels value
print("Accessing and Modifying pixels value in legacy way","\n")
ImageColorValue = img[100,100]
print(ImageColorValue,"\n")

print("Accessing and Modifyind pixels value through array method like array.item and array.itemset\n")

print(img.item(10,10,2))

print("Image shape\n", img.shape)


# cv.imshow("display",img)

# cv.waitKey(0)