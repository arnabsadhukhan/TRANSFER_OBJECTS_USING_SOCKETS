import socket
import time
import pickle
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

HEADERSIZE = 15
print('Ready')


def send(data):
    print('server sending...')
    msg = pickle.dumps(data)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}','utf-8') +msg
    #print('server send ', msg)
    clientsocket.send(msg)
def recv():
    print('server receiving...')
    recv_msg = clientsocket.recv(HEADERSIZE)
    msglen=int(recv_msg)
    #print(msglen)

    recv_msg1 = clientsocket.recv(msglen)
    while len(recv_msg1)<msglen:
        recv_msg1 += clientsocket.recv(msglen-len(recv_msg1))
    return recv_msg1




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

print((socket.gethostname(), 8888))

clientsocket,addr = s.accept()
print(f'connected {addr}')


camera = PiCamera()
camera.resolution = (200, 200)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(200,200))
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
 
    #img = np.random.uniform(size=(200,200),low=1,high=125)
    send(img)
    print('server send')
    r_d = pickle.loads(recv())
    print('result back',r_d)
    rawCapture.truncate(0)
cv2.destroyAllWindows()
