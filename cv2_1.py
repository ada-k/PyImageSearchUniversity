import cv2
import argparse
import numpy as np
import imutils

""" read and save image"""
arg = argparse.ArgumentParser(description='provide paths')
arg.add_argument("--img", default="logo.png") #required=True makes the arg compulsary
arg.add_argument("--save")
args = vars(arg.parse_args())

img = cv2.imread(args["img"])

(h, w, c) = img.shape[:3]
print('height -- no of rows', h)
print('width -- no of cols', w)
print('height -- no of channels', c)
print(c)

cv2.imshow("ada", img)
cv2.imwrite(args["save"], img)
cv2.waitKey(0)

"""getting and setting pixels"""
# recall: 
    # RGB == BGR
    # x,y == y,x

# get pixels
(b,g,r) = img[0, 0]
px = img[150, 123]
print(px)

# set pixels
img[:1000, :1000] = (0, 255, 255)
cv2.imwrite(args["save"], img)


"""drawing"""
# basic drawing

canvas = np.zeros((400, 400, 3), dtype="uint8")
# canvas[:300, :300] = (255, 0, 255)
# cv2.imshow("canvas", canvas)

# line
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.line(canvas, (200,200), (400,400), (0, 255, 255), 10) #the 10 is for the pixel 'thickness'
cv2.imshow("line on canvas", canvas)
cv2.waitKey(0)
#rectangle
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.rectangle(canvas, (200,200), (400,400), (0, 255, 255), -1) #-1 makes it a filled in
cv2.imshow("rect on canvas", canvas)
cv2.waitKey(0)
#circle
canvas = np.zeros((400, 400, 3), dtype="uint8")
(x, y) = (canvas.shape[1]//2, canvas.shape[0]//2)
for r in range(0, 200, 25):
    cv2.circle(canvas, (x,y), r, (255, 45, 111), -1)
cv2.imshow("circle on canvas", canvas)
cv2.waitKey(0)

# image drawing
cv2.circle(img, (30,57), 100, (255, 45, 111), 10)
cv2.imshow("circle on ada", img)
cv2.waitKey(0)

# translation
# 2 lines pf code
img = cv2.imread(args["img"])
m = np.float32([[0,1,30], [1,0,30]]) #down right Tx=30, Ty=30
trans = cv2.warpAffine(img, m, (img.shape[1], img.shape[0]))
trans_ = cv2.warpAffine(img, np.float32([[0,1,-30], [1,0,-30]]), (img.shape[1], img.shape[0]))
cv2.imshow('org', img)
cv2.waitKey(0)
cv2.imshow('transformed', trans)
cv2.waitKey(0)
cv2.imshow('transformed_', trans_) #up left
cv2.waitKey(0)

#  imutils
shifted = imutils.translate(img, 90, 90)
cv2.imshow("right down", shifted)
cv2.waitKey(0)

"""rotation"""
centre = (img.shape[1], img.shape[0])
M = cv2.getRotationMatrix2D(centre, 90, 1)  #add - to 90/degree to rotate clockwise
rotated = cv2.warpAffine(img, M, centre)
cv2.imshow("anticlockwise rotated", rotated)
cv2.waitKey(0)

rotate = imutils.rotate(img, -90)
cv2.imshow("clockwise rotated", rotate)
cv2.waitKey(0)

rotate = imutils.rotate_bound(img, -90)
cv2.imshow("anticlockwise rotated", rotate)
cv2.waitKey(0)

"""resizing"""
## wanna resize to 150px -- width
w = 150
r = w/img.shape[1] # new width as a fraction of org width -- vice versa for height resizing
dim = (w, int(img.shape[0] * r))
# resize
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)

# imutils takes care of the aspect ratio pain
res = imutils.resize(img, height=120)
cv2.imshow("imutils resize", res)
cv2.waitKey(0)


# construct the list of interpolation methods in OpenCV
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# loop over the interpolation methods
for (name, method) in methods:
	# increase the size of the image by 3x using the current
	# interpolation method
	print("[INFO] {}".format(name))
	resized = imutils.resize(img, width=img.shape[1] * 3,
		inter=method)
	cv2.imshow("Method: {}".format(name), resized)
	cv2.waitKey(0)


"""flipping"""
flipped = cv2.flip(img, 1) #1=horizontally, 0=vertically, -1 =both
cv2.imshow("horizontally flipped", flipped)
cv2.waitKey(0)

"""cropping"""
cropped = img[200:2000, 400:3000]
cv2.imshow('cropped', cropped)
cv2.waitKey(0)

"""image arithmetic"""
# images are NumPy arrays stored as unsigned 8-bit integers (unit8)
# with values in the range [0, 255]; when using the add/subtract
# functions in OpenCV, these values will be *clipped* to this range,
# even if they fall outside the range [0, 255] after applying the
# operation
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))

# using NumPy arithmetic operations (rather than OpenCV operations)
# will result in a modulo ("wrap around") instead of being clipped
# to the range [0, 255]
added = np.uint8([200]) + np.uint8([100])
subtracted = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))


image = cv2.imread(args["img"])
cv2.imshow("Original", image)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Lighter", added)
cv2.waitKey(0)

# darker
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)

"""bitwise operations""" 
# -- kinda like sets in calculus
# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# a bitwise 'AND' is only 'True' when both inputs have a value that
# is "ON' --
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

# a bitwise 'OR' examines every pixel in the two inputs, 
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

# both the rectangle and circle are not allowed to *BOTH*
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# bitwise 'NOT' inverts the values of the pixels;
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

"""masking"""
# a mask is the same size as our image, but has only two pixel
# values, 0 and 255 -- pixels with a value of 0 (background) 
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Rectangular Mask", mask)

# apply mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# apply the mask again
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

image = cv2.imread(args["img"])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)