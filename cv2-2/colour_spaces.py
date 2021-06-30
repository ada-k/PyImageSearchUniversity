import cv2
import argparse
import imutils
import numpy

"""command line arguments"""
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", default = "/home/ada/pyimagesearch/PyImageSearchUniversity/cv2-2/adrian.png")
arg.add_argument("-o", "--path", default = "save.png")
args = vars(arg.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("RGB", image)
cv2.waitKey(0)

# loop over channels and display them
for (name, chan) in zip(('B', 'G', 'R'), cv2.split(image)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# convert to hsv and display
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

for (name, chan) in zip(('H', 'S', 'V'), cv2.split(hsv)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# convert to L*a*b and display
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("Lab", lab)
cv2.waitKey(0)

for (name, chan) in zip(('L', 'A', 'B'), cv2.split(lab)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()

# gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale", gray)
cv2.waitKey(0)
