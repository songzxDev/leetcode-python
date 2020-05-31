# -*- coding:utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://localhost:5555')
socket.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
while True:
    resp = socket.recv()
    print "response is : %s" % resp
