import socket
import pickle
import cv2
import requests
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

HEADERSIZE = 15
def send(data):
    print('client sending...')

    msg = pickle.dumps(data)
    print('send len',len(msg))
    msg = bytes(f'{len(msg):<{HEADERSIZE}}','utf-8') +msg
    #print(msg[:100])
    s.send(msg)
def recv():
    print('client receiving...')  
    recv_msg = s.recv(HEADERSIZE)
    msglen=int(recv_msg)
    recv_msg = s.recv(msglen)
    while len(recv_msg)<msglen:
        recv_msg += s.recv(msglen-len(recv_msg))
    return recv_msg



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    recv_msg = recv()
    img = pickle.loads(recv_msg)

    cv2.imshow('img',img)

    if cv2.waitKey(1)==27:
        break
    print('server received data')

    
    r= ['get image']
    send(r)
    print('server send data')



    

cv2.destroyAllWindows()