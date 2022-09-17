import zmq
import cv2

from common.env import EDGE_LISTEN_ADDRESS

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect(EDGE_LISTEN_ADDRESS)

camera = cv2.VideoCapture(0)

while True:
    try:
        (grabbed, frame) = camera.read()
        encoded, buffer = cv2.imencode(".jpg", frame)
        socket.send(buffer)

    except KeyboardInterrupt:
        socket.close()
        context.term()
        camera.release()
        cv2.destroyAllWindows()

        print("Exited!")

        break