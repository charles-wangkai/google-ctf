1. `node baseDecoder.js`

1. `python3 unhexlify.py base_decoded.txt base_decoded_unhexlified.jpg`

1. `python3 exif.py`

1. Check out ["evil" programming language](https://esolangs.org/wiki/Evil)

1. From [the evil home page](http://web.archive.org/web/20070103000858/www1.pacific.edu/~twrensch/evil/index.html), download [Java implementation of an evil interpreter](http://web.archive.org/web/20070103000858/www1.pacific.edu/~twrensch/evil/evil.java) to `evil.java`

1. `java evil.java exif.evl > evil_output.txt`

1. `python3 unhexlify.py evil_output.txt evil_output_unhexlified.zlib`

1. `python3 zlib_decompress.py evil_output_unhexlified.zlib evil_zlib_decompressed.gz`

1. `gunzip -c evil_zlib_decompressed.gz > gzip_decompressed.ppm`

1. Check out ["Piet" programming language](https://esolangs.org/wiki/Piet)

1. Use [npiet online](https://www.bertnase.de/npiet/npiet-execute.php) to get the output for `gzip_decompressed.ppm` and save it to `piet_output.txt`

1. `python3 unhexlify.py piet_output.txt piet_output_unhexlified.zlib`

1. `python3 zlib_decompress.py piet_output_unhexlified.zlib piet_zlib_decompressed.txt`

1. Check out ["nya~" programming language](https://esolangs.org/wiki/Nya~)

1. Download and build [official implementation of nya~](https://github.com/sech1p/nya)

1. `nya/build/nya piet_zlib_decompressed.txt > nya_output.unary`

1. `python3 unary_to_brainfuck.py nya_output.unary unary_output.brainfuck`

1. Check out ["brainfuck" programming language](https://esolangs.org/wiki/Brainfuck)

1. Use [El Brainfuck](https://copy.sh/brainfuck/) to get the output for `unary_output.brainfuck`

> CTF{pl34s3_n0_m04r}
