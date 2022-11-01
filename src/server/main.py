import base64
import time
import zmq
import cv2
import numpy as np

from src.common.env import SERVER_LISTEN_ADDRESS

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.RCVHWM, 2)
socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.connect(SERVER_LISTEN_ADDRESS)

while True:
    try:
        frame = socket.recv_pyobj() 
        cv2.imshow("Received frame", frame)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        socket.close()
        context.term()
        cv2.destroyAllWindows()

        print("Exited!")

        break