# -*- coding: utf-8 -*
from twisted.internet.protocol import Protocol


class SybilServerTcpBinProtocol(Protocol):

    def __init__(self, sybilBrain):
        self.sybilBrain = sybilBrain

    def dataReceived(self, data):
        
