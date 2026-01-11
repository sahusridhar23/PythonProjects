import cv2 as cv
from pygments.formatters import img


print("Welcome to Image Resizer 1.0 . Created by sridhar sahu")

img = cv.imread("coffee.jpeg")

# cv.imshow("display window",img)
# cv.waitKey(0)

#percent by which item is resized
scale_percent = 200

#calac 150% of original dimensions
new_height = int(img.shape[0] * scale_percent / 100)
new_width = int(img.shape[1] * scale_percent / 100)

#resize
dim = (new_width, new_height)
img_resize = cv.resize(img, dim)
cv.imwrite("coffee_resized.jpeg", img_resize)
cv.waitKey(0)

#Original vs resized
cv.imshow("original", img)
img2 = cv.imread("coffee_resized.jpeg")
cv.imshow("resized", img2)
cv.waitKey(0)