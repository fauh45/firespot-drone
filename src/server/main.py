import zmq
import cv2
import numpy as np

from common.env import SERVER_LISTEN_ADDRESS

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(SERVER_LISTEN_ADDRESS)
socket.subscribe("")

while True:
    try:
        raw_image = socket.recv()
        image = np.frombuffer(raw_image, dtype=np.uint8)
        frame = cv2.imdecode(image, 1)
        cv2.imshow("Received frame", frame)
        
    except KeyboardInterrupt:
        socket.close()
        context.term()
        cv2.destroyAllWindows()

        print("Exited!")

        break