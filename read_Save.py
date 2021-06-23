import cv2
import argparse
import numpy as np

"""# read and save image"""
arg = argparse.ArgumentParser(description='provide paths')
arg.add_argument("--img", required=True)
arg.add_argument("--save", required=True)
args = vars(arg.parse_args())

img = cv2.imread(args["img"])

(h, w, c) = img.shape[:3]
print('height -- no of rows', h)
print('width -- no of cols', w)
print('height -- no of channels', c)
print(c)

# cv2.imshow("ada", img)
# cv2.imwrite(args["save"], img)
# cv2.waitKey(0)

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

