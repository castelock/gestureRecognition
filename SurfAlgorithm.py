import cv2
import numpy as np

# Open Camera object
cap = cv2.VideoCapture(0)


# while True:
#     # Grab the current frame
#     (grabbed, frame) = cap.read()
#
#     grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Create the SURF descriptor
#     surf = cv2.xfeatures2d.SURF_create()
#     # Get the keypoints
#     keypoints,	descriptor	=	surf.detectAndCompute(grayPic,None)
#     # Draw the keypoints
#     grayPic = cv2.drawKeypoints(image=grayPic,	outImage=grayPic,	keypoints	=	keypoints,
#     flags =	cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,	color	=	(51,	163,	236))
#     # Show the image
#     cv2.imshow('Surf Algorithm', grayPic)

    # Grab the current frame
(grabbed, frame) = cap.read()

grayPic = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Create the SURF descriptor
surf = cv2.xfeatures2d.SURF_create()
    # Get the keypoints
keypoints, descriptor = surf.detectAndCompute(grayPic, None)
    # Draw the keypoints
grayPic = cv2.drawKeypoints(image=grayPic, outImage=grayPic, keypoints=keypoints,
                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(51, 163, 236))
    # Show the image
cv2.imshow('Surf Algorithm', grayPic)
cv2.imwrite('SURF_hand.png',grayPic)

while True:
    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()