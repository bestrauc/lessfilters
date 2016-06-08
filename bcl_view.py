#!/usr/bin/env python3

import sys
import struct
from math import log, ceil

with open(sys.argv[1], "rb") as bcl_file:
    # get the number of bases
    data = bcl_file.read(4)
    n = struct.unpack("<i", data)[0]
    print("Length", n)
    n_len = ceil(log(n,10))

    print("{:^}\t{:^}\t{:^}\t{:^}".format("Read", "Base", "Qual", "Raw")) 

    # mask for the first two bits (encodes bases)
    mask = 0b11
    for i in range(0,n):
        raw = ord(bcl_file.read(1))
        base = int(raw & mask)
        qual = int(raw >> 2)
        if base == 0:
            baseChar = 'A'
        elif base == 1:
            baseChar = 'C'
        elif base == 2:
            baseChar = 'G'
        elif base == 3:
            baseChar = 'T'

        print(("{:>%id}\t{}\t{}\t{}"%n_len).format(i+1, baseChar, qual, hex(raw)))
       

