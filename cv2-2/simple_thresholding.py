import cv2
import argparse
import imutils
import numpy

"""command line arguments"""
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", default = "/home/ada/pyimagesearch/PyImageSearchUniversity/images/coins01.png")
arg.add_argument("-o", "--path", default = "save.png")
args = vars(arg.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("original", image)
cv2.waitKey(0)

# preprocessing: grayscale then slightly blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (7, 7), 0)

# inverse thresholding
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV) # 200 == threshold test, 255 == BLACK OR WHITE
cv2.imshow("threshold binary inverse", threshInv)
cv2.waitKey(0)

# normal thresholding
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY) 
cv2.imshow("threshold binary", thresh)
cv2.waitKey(0)

# bitwise op
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)