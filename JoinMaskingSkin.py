# import the necessary packages
import sys
import numpy
import cv2

# load the video
camera = cv2.VideoCapture(0)
# Limits
skin_ycrcb_mint = numpy.array((0, 133, 77))
skin_ycrcb_maxt = numpy.array((255, 173, 127))

while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    im_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    skin_ycrcb = cv2.inRange(im_ycrcb, skin_ycrcb_mint, skin_ycrcb_maxt)

    # DEBUG INIT
    # apply a series of erosions and dilations to the mask
    # using an elliptical kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    skin_ycrcb = cv2.erode(skin_ycrcb, kernel, iterations=2)
    skin_ycrcb = cv2.dilate(skin_ycrcb, kernel, iterations=2)

    # blur the mask to help remove noise, then apply the
    # mask to the frame
    skin_ycrcb = cv2.GaussianBlur(skin_ycrcb, (3, 3), 0)
    #skin = cv2.bitwise_and(frame, frame, mask=skin_ycrcb)
    # DEBUG END

    (_ ,contours, _) = cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #(_, contours, _) = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)



    for i, c in enumerate(contours):
        area = cv2.contourArea(c)
        if area > 1000:
            cv2.drawContours(frame, contours, i, (255, 0, 0), 3)



    # show the image
    cv2.imshow("images", frame)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()