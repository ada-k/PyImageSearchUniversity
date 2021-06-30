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
cv2.imshow("original", image)
cv2.imshow("single channel", gray)
cv2.waitKey(0)