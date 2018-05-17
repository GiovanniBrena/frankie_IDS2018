import cv2
img = cv2.imread("img/1.jpg")
crop_img = img[0:100, 0:100]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)