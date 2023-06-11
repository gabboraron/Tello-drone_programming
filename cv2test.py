
import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
if img is None:
    sys.exit("Could not read the image.")

cv.namedWindow("night")
cv.imshow("night", img)
#cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imshow("night", img)
    #cv.imwrite("starry_night.png", img)