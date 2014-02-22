# -*- coding: utf-8 -*-
from twisted.internet.protocol import DatagramProtocol
import ctypes
import struct

class SybilServerUdpBinProtocol(DatagramProtocol):

    def __init__(self, sybilBrain):
        self.sybilBrain = sybilBrain

    def datagramReceived(self, datagram, (host,port)):
        print "received %r from %s:%d" % (raw_data, host, port)
        length = len(datagram)
        fmt = 'IH'+format(length)+'s'
        raw_data = struct.unpack_from('IH'+fmt+'s',datagram[0:])
        query = raw_data[6:]
        response = self.sybilBrain.generateResponse(query)

        buff = ctypes.create_string_buffer(6+length)
        timeInSeconds = time.time()
        struct.pack_into(fmt, buff, 0, timeInSeconds, length, line)
        self.transport.write(buff, (self.server_host,self.server_port))
     

