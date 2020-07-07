# -*- coding:utf-8 -*-
import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

while True:
    getinput = input('please write anything: ')
    if getinput == 'exit':
        sys.exit()
    socket.send(getinput)
    message = socket.recv()

    print "Received reply: %s" % message
