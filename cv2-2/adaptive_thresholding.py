import cv2
import argparse
import imutils
import numpy

"""command line arguments"""
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", default = "/home/ada/pyimagesearch/PyImageSearchUniversity/images/steve_jobs.png")
arg.add_argument("-o", "--path", default = "save.png")
args = vars(arg.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("original", image)
cv2.waitKey(0)

# preprocessing: grayscale then slightly blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (7, 7), 0)

# apply simple thresholding with a hardcoded threshold value
(T, threshInv) = cv2.threshold(blurred, 230, 255,
	cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Thresholding", threshInv)
cv2.waitKey(0)

# apply Otsu's automatic thresholding
(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", threshInv)
cv2.waitKey(0)


# instead of manually specifying the threshold value, we can use
# adaptive thresholding to examine neighborhoods of pixels and
# adaptively threshold each neighborhood
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Mean Adaptive Thresholding", thresh)
cv2.waitKey(0)

# perform adaptive thresholding again, this time using a Gaussian
# weighting versus a simple mean to compute our local threshold
# value
thresh = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Gaussian Adaptive Thresholding", thresh)
cv2.waitKey(0)