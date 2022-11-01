import base64
from distutils.archive_util import make_archive
from cv2 import cvtColorTwoPlane
from numpy import nanstd
import zmq
import cv2

from src.common.env import EDGE_LISTEN_ADDRESS, SEND_VIDEO_DATA
from src.edge.constants import lower_lower_red, lower_upper_red, upper_lower_red, upper_upper_red

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.SNDHWM, 2)
socket.bind(EDGE_LISTEN_ADDRESS)

camera = cv2.VideoCapture(0)
detector = cv2.SimpleBlobDetector()

while True:
    try:
        grabbed, frame = camera.read()
        frame = cv2.resize(frame, (480, 360))

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask0 = cv2.inRange(hsv_frame, lower_lower_red, lower_upper_red)
        mask1 = cv2.inRange(hsv_frame, upper_lower_red, upper_upper_red)
        mask = mask0 + mask1

        if not SEND_VIDEO_DATA:
            cv2.imshow("Original Image", frame)
            cv2.imshow("Masked image", mask)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            # the contours are drawn here
            cv2.drawContours(frame, contours, -1, 255, 3)

            #find the biggest area of the contour
            c = max(contours, key = cv2.contourArea)

            x, y, w, h = cv2.boundingRect(c)
            # draw the 'human' contour (in green)
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)

            center_x = x + int(0.5 * w)
            center_y = y + int(0.5 * h)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), 5)

        if not SEND_VIDEO_DATA:
            cv2.imshow("Biggest Blob", frame)

        if SEND_VIDEO_DATA:
            encoded, buffer = cv2.imencode(".jpg", frame)
            socket.send_pyobj(frame)

        if not SEND_VIDEO_DATA:
            cv2.waitKey(1)

    except KeyboardInterrupt:
        socket.close()
        context.term()
        camera.release()
        cv2.destroyAllWindows()

        print("Exited!")

        break