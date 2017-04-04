import cv2
import numpy as np

# Open Camera object
cap = cv2.VideoCapture(0)

# INCLUIR ESTO EN UN LOOP Y OBTENER UNA IMAGEN DE LA CÁMARA EN CADA FRAME PARA USAR SURF
grayPic = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
# Create the SURF descriptor
surf = cv2.xfeatures2d.SURF_create()
# Get the keypoints
keypoints,	descriptor	=	surf.detectAndCompute(grayPic,None)
# Draw the keypoints
grayPic = cv2.drawKeypoints(image=grayPic,	outImage=grayPic,	keypoints	=	keypoints,
flags	=	cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINT,	color	=	(51,	163,	236))

cv2.imshow('Surf Algorithm',grayPic)

while(True):
    if cv2.waitKey(1) & 0xff == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()