import cv2
#from cv2 import cv

#method = cv.CV_TM_SQDIFF_NORMED
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Read the images from the file
small_image = cv2.imread('img/2_rot.jpg')
large_image = cv2.imread('img/1.jpg')

result = cv2.matchTemplate(small_image, large_image, 1)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
#cv2.imshow('output',large_image)

cv2.imwrite('out.png',large_image)

# The image is only displayed if we call this
#cv2.waitKey(0)