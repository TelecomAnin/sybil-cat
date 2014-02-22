# -*- coding: utf-8 -*-
from twisted.internet.protocol import DatagramProtocol
import time


class SybilServerUdpTextProtocol(DatagramProtocol):

    def __init__(self, sybilBrain):
        self.sybilBrain = sybilBrain

    def datagramReceived(self, datagram, address):
        print "received datagram : %r" %(datagram)
        start_index=datagram.find(':')+1
        if (len(datagram)<start_index):
            raise  Exception("Oops! There is a problem with the received packet")
        query=datagram[start_index:len(datagram)]
        response=self.sybilBrain.generateResponse(query)

        timeInSeconds = time.time()
        data = format(timeInSeconds) + ':' + response

        self.transport.write(data, address)
     

