import cv2
import numpy as np
from matplotlib import pyplot as plt


def evaluate_img_diff(img1,img2):

    return 0


img = cv2.imread('img/1.jpg',0)
imgOriginal = img.copy()
img2 = img.copy()
img2 = cv2.medianBlur(img2,5)
img2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

template = cv2.imread('img/2_rot.jpg',0)
templateOriginal = template.copy()
template = cv2.medianBlur(template,5)
template = cv2.adaptiveThreshold(template,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


img = img2.copy()
method = eval(methods[0])

# Apply template Matching
res = cv2.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

'''
y = top_left[1]
x = top_left[0]
crop_img = img[y:y + h, x:x + w]
cv2.imshow("cropped", crop_img)
evaluate_img_diff(template,crop_img)
'''

titles = ['Original Image', 'Original Pattern',
          'Matching Result', 'Threshold Pattern']
images = [imgOriginal, templateOriginal, img, template]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

