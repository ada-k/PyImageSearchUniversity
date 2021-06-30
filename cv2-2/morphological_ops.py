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

# applying a series of erosions  -- application - disconnecting components e.g when u wanna count coins or pills
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations = i+1) #None arg is the structuring element == kernels: 3*3, circular, cross...
    cv2.imshow(f"{i} - eroded", eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)


# dialation == enalrging image foreground - used to counter erosion
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations = i+1) #None default == 3*3 kernel
    cv2.imshow(f"{i} - dilated", dilated)
    cv2.waitKey(0)

# clean up the screen
cv2.destroyAllWindows()
cv2.imshow("original", image)

# opening - removing noise.
kernel_sizes = [(3,3), (5,5), (7,7)]
for kernel in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel) # construct a rectangular kernel
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel) # applying an opening operation
    cv2.imshow(f"{kernel} - opening", opening)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)

#closing - dilation followed by erosion == opp of opening
for kernel in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel) # construct a rectangular kernel
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel) # applying an opening operation
    cv2.imshow(f"{kernel} - closing", closing)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)

# morphological gradient: minus dilation and erosion == detection of foreground vs background pixels
for kernel in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel) # construct a rectangular kernel
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel) # applying an opening operation
    cv2.imshow(f"{kernel} - gradient", gradient)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)
