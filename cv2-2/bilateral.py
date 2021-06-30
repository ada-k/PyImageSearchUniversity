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
cv2.imshow("original", image)
cv2.waitKey(0)

## reduces noise but maintains edges. -- introduces 2 gaussian dists: 
### spatial neigbours and pixel intensity
#### used in image cartoonisation
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f"{(diameter, sigmaColor, sigmaSpace)} - bilateral blurred", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)

