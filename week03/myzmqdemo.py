# -*- coding:utf-8 -*-
import zmq

import sys

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    try:
        print 'wait for client message......'
        message = socket.recv()
        print 'message from client is: %s' % message
        socket.send(message)
    except Exception as ex:
        print ex
        sys.exit()
