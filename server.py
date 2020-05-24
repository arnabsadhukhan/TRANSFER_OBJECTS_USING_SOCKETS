import socket
import time
import pickle
import numpy as np
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


while True:

    img = np.random.uniform(size=(200,200),low=1,high=125)
    send(img)
    print('server send')
    r_d = pickle.loads(recv())
    print('result back',r_d)


cv2.destroyAllWindows()