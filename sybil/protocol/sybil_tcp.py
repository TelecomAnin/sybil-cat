# -*- coding: utf-8 -*-
import ctypes
import struct

def pack(line):
    length = len(line)
    buff = ctypes.create_string_buffer(6+length)
    timeInSeconds = time.time()
    fmt = 'IH'+format(length)+'s'
    struct.pack_into(fmt, buff, 0, timeInSeconds, length, line)
    return buff
