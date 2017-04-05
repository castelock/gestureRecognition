import cv2
import numpy as np

# Open Camera object
cap = cv2.VideoCapture(0)


# while True:
#     # Grab the current frame
#     (grabbed, frame) = cap.read()
#
#     grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Create the SIFT descriptor
#     sift = cv2.xfeatures2d.SIFT_create()
#     # Get the keypoints
#     keypoints,	descriptor	=	sift.detectAndCompute(grayPic,None)
#     print ("Length: "+ str(len(keypoints)))
#     # Show the image
#     cv2.imshow('Sift Algorithm', grayPic)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

    # Grab the current frame
(grabbed, frame) = cap.read()

grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Create the SIFT descriptor
mser = cv2.MSER_create()
    # Get the keypoints
regions	=	mser.detectRegions(grayPic,None)
print("Length Regions:"+ str(len(regions)))
# Draw contours
cv2.drawContours(grayPic, regions, -1, (0,255,0), 3)
    # Draw the keypoints
# grayPic = cv2.drawKeypoints(image=grayPic, outImage=grayPic, keypoints=keypoints,
#                             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(51, 163, 236))
    # Show the image
cv2.imshow('MSER Algorithm', grayPic)
cv2.imwrite('MSER_hand.png',grayPic)

while True:
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()