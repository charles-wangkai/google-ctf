import binascii
import struct


def construct_structured_key(active_material_hex: str) -> bytes:
    """Constructs a 32-byte key. If structured, uses 16 bytes of active material."""  # inserted
    key_words_int = [0] * 8
    if len(active_material_hex) != 32:
        raise ValueError(
            "For patterned keys ('pattern_a', 'pattern_b'), active_material_hex must be 16 bytes (32 hex characters)."
        )
    active_material_bytes = bytes.fromhex(active_material_hex)
    am_idx = 0

    def get_am_word():
        nonlocal am_idx  # inserted
        if am_idx + 4 > len(active_material_bytes):
            raise ValueError("Not enough active material for the 4 active key words.")
        word = int.from_bytes(active_material_bytes[am_idx : am_idx + 4], "little")
        am_idx += 4
        return word

    key_words_int[1] = get_am_word()
    key_words_int[3] = get_am_word()
    key_words_int[4] = get_am_word()
    key_words_int[6] = get_am_word()
    key_bytes_list = []
    for word_int in key_words_int:
        key_bytes_list.append(word_int.to_bytes(4, "little"))
    return b"".join(key_bytes_list)


known_key_active_material_hex = "5c54700231f4727bf7d49234e7bbb1c9"
known_structured_key_bytes = construct_structured_key(known_key_active_material_hex)
known_structured_key_hex = known_structured_key_bytes.hex()

print("known_structured_key_bytes:", known_structured_key_bytes)
print("known_structured_key_hex:", known_structured_key_hex)


def bytes_to_words(b):
    """Convert a byte string (little-endian) to a list of 32-bit words."""  # inserted
    if len(b) % 4 != 0:
        raise ValueError(
            "Input bytes length must be a multiple of 4 for word conversion."
        )
    return list(struct.unpack("<" + "I" * (len(b) // 4), b))


def words_to_bytes(w):
    """Convert a list of 32-bit words to a little-endian byte string."""  # inserted
    return struct.pack("<" + "I" * len(w), *w)


def rotl32(v, c):
    """Rotate a 32-bit unsigned integer left by c bits."""  # inserted
    v &= 4294967295
    return v << c & 4294967295 | v >> 32 - c


def add32(a, b):
    """Add two 32-bit unsigned integers, wrapping modulo 2^32."""  # inserted
    return a + b & 4294967295


def mix_bits(state_list, a_idx, b_idx, c_idx, d_idx):
    """\n    Mixes Bits. Modifies state_list in-place.\n"""  # inserted
    a, b, c, d = (
        state_list[a_idx],
        state_list[b_idx],
        state_list[c_idx],
        state_list[d_idx],
    )
    a = add32(a, b)
    d ^= a
    d = rotl32(d, 16)
    c = add32(c, d)
    b ^= c
    b = rotl32(b, 12)
    a = add32(a, b)
    d ^= a
    d = rotl32(d, 8)
    c = add32(c, d)
    b ^= c
    b = rotl32(b, 7)
    state_list[a_idx], state_list[b_idx], state_list[c_idx], state_list[d_idx] = (
        a,
        b,
        c,
        d,
    )


def make_block(
    key_bytes, nonce_bytes, counter_int, current_constants_tuple, rounds_to_execute=8
):
    """\n    Generates one 64-byte block of bits, allowing control over the\n    number of rounds executed.\n"""  # inserted
    if len(key_bytes) != 32:
        raise ValueError("Key must be 32 bytes")
    if len(nonce_bytes) != 12:
        raise ValueError("Nonce must be 12 bytes")
    if not 1 <= rounds_to_execute <= 8:
        raise ValueError(
            "rounds_to_execute must be between 1 and 8 for this modified version."
        )
    state = [0] * 16
    state[0:4] = current_constants_tuple
    try:
        key_words = bytes_to_words(key_bytes)
        nonce_words = bytes_to_words(nonce_bytes)
    except ValueError as e:
        pass  # postinserted
    else:  # inserted
        state[4:12] = key_words
        state[12] = counter_int & 4294967295
        state[13:16] = nonce_words
        initial_state_snapshot = list(state)
        qr_operations_sequence = [
            lambda s: mix_bits(s, 0, 4, 8, 12),
            lambda s: mix_bits(s, 1, 5, 9, 13),
            lambda s: mix_bits(s, 2, 6, 10, 14),
            lambda s: mix_bits(s, 0, 5, 10, 15),
            lambda s: mix_bits(s, 2, 7, 8, 13),
            lambda s: mix_bits(s, 3, 4, 9, 14),
        ]
        for i in range(rounds_to_execute):
            qr_operations_sequence[i](state)
    for i in range(16):
        state[i] = add32(state[i], initial_state_snapshot[i])
    return words_to_bytes(state)


current_constants_tuple = [0, 0, 0, 0]
key_words = bytes_to_words(known_structured_key_bytes)
print("key_words:", key_words)

counter_int = 0
nonce_words = [0, 0, 0]

state = current_constants_tuple + key_words + [counter_int] + nonce_words

keystream_block = words_to_bytes(state)
print("keystream_block:", keystream_block)
print(len(keystream_block))

key_bytes = known_structured_key_bytes
nonce_bytes = words_to_bytes(nonce_words)
current_counter = counter_int
rounds_to_execute = 1

keystream_block = make_block(
    key_bytes,
    nonce_bytes,
    current_counter,
    current_constants_tuple,
    rounds_to_execute=rounds_to_execute,
)
print(keystream_block)


flag_ciphertext = "692f09e677335f6152655f67304e6e40141fa702e7e5b95b46756e63298d80a9bcbbd95465795f21ef0a"
# flag_ciphertext = "1227095654657374466c61675f303030a48a9ad48898d0343030303052d8d5c62bcb280930303030fe0a"
flag_cipher_bytes = binascii.unhexlify(flag_ciphertext)
print("flag_cipher_bytes:", flag_cipher_bytes)


flag_prefix = b"CTF{"


current_counter = 0
while True:
    if current_counter % 1_000_000 == 0:
        print("searching: ", current_counter)

    keystream_block = make_block(
        key_bytes,
        nonce_bytes,
        current_counter,
        current_constants_tuple,
        rounds_to_execute=rounds_to_execute,
    )
    # print(keystream_block)

    output_bytes = [flag_prefix[i] ^ keystream_block[i] for i in range(4)]
    # print("output_bytes:", output_bytes)
    if output_bytes == list(flag_cipher_bytes[:4]):
        print("Found!")
        print("current_counter:", current_counter)

        break

    current_counter += 1
