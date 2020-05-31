# -*- coding:utf-8 -*-

import zmq
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5555')

while True:
    msg = input('please input you want to publish message: ').strip()
    if msg == 'exit':
        sys.exit()
    socket.send(msg.encode('utf-8'))
    time.sleep(1)
