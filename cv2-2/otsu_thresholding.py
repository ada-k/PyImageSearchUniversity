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

# apply Otsu's automatic thresholding which automatically determines
# the best threshold value
(T, threshInv) = cv2.threshold(blurred, 0, 255,	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# bitwise
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)