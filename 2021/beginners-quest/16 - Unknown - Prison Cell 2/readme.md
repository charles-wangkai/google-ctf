> Reference: https://github.com/Dvd848/CTFs/blob/master/2021_GoogleCTF_BQ/16_Unknown_-_Prison_Cell_2.md

1. `echo -n "gctf" > prefix`

1. `fastcoll -p prefix`

1. `xxd -p msg1.bin | tr -d '\n'`

1. `xxd -p msg2.bin | tr -d '\n'`

> CTF{h4sh_m3_tw1c3_1245fd3}
