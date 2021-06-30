import cv2
import argparse
import imutils
import numpy

"""command line arguments"""
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", default = "logo.png")
arg.add_argument("-o", "--path", default = "save.png")
args = vars(arg.parse_args())

image = cv2.imread(args['image'])
# convert image to grayscale -- single channel image.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

# top/white hat - reveal bright regions of an image in a dark background
# black hat - reveal dark regions in a bright background.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5)) # construct a rectangular kernel respective of the image appearance
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("original", image)
cv2.imshow("single channel", gray)
cv2.imshow("blackhat", blackhat)
cv2.imshow("tophat", tophat)
cv2.waitKey(0)



