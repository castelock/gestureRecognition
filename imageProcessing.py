import cv2
import  numpy as np


cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    _, frame = cap.read()

    # Save an image from the webcam
    cv2.imwrite("Openhand.png",frame)

    # Convert to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #cv2.imshow("HSV",hsv)

  # Convert to Gray
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold
    # ret, thresh = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Threshold", thresh)

# Adaptive Threshold
#     threshGaussian = cv2.adaptiveThreshold(grayScale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
#     cv2.imshow("Adaptive Threshold", threshGaussian)
    # Applying an opening transformation
    # kernel = np.ones((5, 5), np.uint8)
    # opening= cv2.morphologyEx(threshGaussian, cv2.MORPH_OPEN, kernel)
    # cv2.imshow("Opening", opening)
    # Applying an closing transformation
    # kernel = np.ones((5, 5), np.uint8)
    # closing = cv2.morphologyEx(threshGaussian, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow("Closing", closing)

#     cv2.imwrite("MypictureGauss.png",threshGaussian)
#     threshMean = cv2.adaptiveThreshold(grayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#     cv2.imshow("Adaptive Threshold Mean", threshMean)
#     cv2.imwrite("MypictureMean.png", threshMean)

    # Otsu's thresholding after Gaussian filtering
    # blur = cv2.GaussianBlur(grayScale, (5, 5), 0)
    # ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("Otsu's thresholding", th3)

    # Laplacian Gradient
    # laplacian = cv2.Laplacian(grayScale, cv2.CV_64F)
    # cv2.imshow("Laplacian",laplacian)

    # Canny Edge Detection
    # edges = cv2.Canny(grayScale, 100, 200)
    # cv2.imshow("Cany", edges)

# Contours
#     ret, thresh = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)
#     image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("Contours",image)
    # Drawing contours
    # imgDraw1 = cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)
    # cv2.imshow("Drawing Contours", imgDraw1)
    # cnt = contours[4]
    # imgDraw2 = cv2.drawContours(thresh, [cnt], 0, (0, 255, 0), 3)
    # cv2.imshow("Last Drawing Contours", imgDraw2)

    # Moments
    # ret, thresh = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)
    # image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    # cnt = contours[0]
    # M = cv2.moments(cnt)
    # print M

    # Contour area
    # area = cv2.contourArea(contours[4])
    # cv2.imshow("Contour Area",area)

    # Convex Hull
    # hull = cv2.convexHull(contours[0])
    # cv2.imshow("Convex Hull", hull)

    c = cv2.waitKey(0)
    if 'q' == chr(c & 255):
        break

cap.release()
cv2.destroyAllWindows()
