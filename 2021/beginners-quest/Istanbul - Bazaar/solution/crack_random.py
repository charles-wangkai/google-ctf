from randcrack import RandCrack

rc = RandCrack()

for line in open('resources/8d19115532225f6ab25ed208e355b37d55476dfc2c1996cbe81f6e82c96f79a20756d5d53fac7f90bc7841aedab34d0686335bafcdbe2cf07333163719ecff9b/robo_numbers_list.txt'):
    rc.submit(int(''.join(line.strip().split('-'))) - (1 << 31))

with open('resources/8d19115532225f6ab25ed208e355b37d55476dfc2c1996cbe81f6e82c96f79a20756d5d53fac7f90bc7841aedab34d0686335bafcdbe2cf07333163719ecff9b/secret.enc', 'rb') as f:
    data = f.read()
    print(bytes([b ^ rc.predict_getrandbits(8) for b in data]).decode())
