import sys

DIGIT_TO_BRAINFUCK = {
    '0': '>',
    '1': '<',
    '2': '+',
    '3': '-',
    '4': '.',
    '5': ',',
    '6': '[',
    '7': ']'
}

with open(sys.argv[1], 'r') as in_file:
    with open(sys.argv[2], 'w') as out_file:
        out_file.write(
            ''.join(DIGIT_TO_BRAINFUCK[d] for d in oct(int(in_file.read()))[3:]))
