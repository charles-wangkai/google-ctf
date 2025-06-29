import re
import string
import subprocess

KNOWN_KEY_ACTIVE_MATERIAL_HEX = "5c54700231f4727bf7d49234e7bbb1c9"
SECRET_TARGET_NONCE_HEX = "000000010000000000000000"
SECRET_TARGET_COUNTER_INT = 32279

target_flag_ciphertext = "692f09e677335f6152655f67304e6e40141fa702e7e5b95b46756e63298d80a9bcbbd95465795f21ef0a"


for c in string.printable:
    with open("flag.txt", "w") as flag_file:
        flag_file.write("CTF{w3_aRe_g0Nn@_ge7_MY_FuncKee_monkey_!!" + c)

    subprocess.run(["sh", "init.sh"])

    with open("ctf_challenge_package.json", "r") as result_file:
        flag_ciphertext = re.search(
            r'"flag_ciphertext": "(.*)"', result_file.read()
        ).group(1)

        if target_flag_ciphertext.startswith(flag_ciphertext):
            print("Found!")
            print("c:", c)

            break
