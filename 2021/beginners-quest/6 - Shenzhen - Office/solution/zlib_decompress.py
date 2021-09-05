import sys
import zlib

with open(sys.argv[1], 'rb') as in_file:
    with open(sys.argv[2], 'wb') as out_file:
        out_file.write(zlib.decompress(in_file.read()))
