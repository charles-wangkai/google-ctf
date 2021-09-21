> Reference: https://github.com/Dvd848/CTFs/blob/master/2021_GoogleCTF_BQ/9_Johannesburg_-_Hideout.md

1. `jadx -d output ../resources/06f923cd67e28af3d409ff78fd8385ae6457f4ea153a827e9a39c57293b7832e5064e75b4c48c1ac95bd62504a495258a04baec89e813eba7758fb88db329ca8/gCTF.apk`

2. Open `../resources/06f923cd67e28af3d409ff78fd8385ae6457f4ea153a827e9a39c57293b7832e5064e75b4c48c1ac95bd62504a495258a04baec89e813eba7758fb88db329ca8/bzImage.elf` in [Ghidra](https://ghidra-sre.org/)

3. Check the decompiled code for the function `sys_write()`

> CTF{SB:575756}
