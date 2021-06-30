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

image = cv2.imread(args['image'])
cv2.imshow("original", image)
cv2.waitKey(0)

kernel_sizes = [(3,3), (9,9), (15,15)] # the larger the kernel, the blurrier the image - can be rect as long as the values are odd

# basic avg blur
for (kx, ky) in kernel_sizes:
    blurred = cv2.blur(image, (kx, ky))
    cv2.imshow(f"{(kx, ky)} - blurred", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)

# Gaussian Blur  -  #gives more weight to the pixels at the centre of the kernel
for (kx, ky) in kernel_sizes:
    gaussian_blurred = cv2.GaussianBlur(image, (kx, ky), 0) # 0 tells cv2 to automatically compute sigma using our kernel size
    cv2.imshow(f"{(kx, ky)} - gaussian_blurred", gaussian_blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)

# Median Blur  - 
for k in (3, 9, 15):
    median_blurred = cv2.medianBlur(image, k) # 0 tells cv2 to automatically compute sigma using our kernel size
    cv2.imshow(f"{(kx, ky)} - median_blurred", median_blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("original", image)