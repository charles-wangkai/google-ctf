import binascii
import sys

with open(sys.argv[1], 'r') as in_file:
    with open(sys.argv[2], 'wb') as out_file:
        out_file.write(binascii.unhexlify(in_file.read()))
