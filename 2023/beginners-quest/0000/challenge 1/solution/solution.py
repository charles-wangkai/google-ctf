def main():
    keys = [24, 0, 22, 8, 0, 9]
    key_index = 0

    cipher_text = "Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}"

    plain_text = ""
    for c in cipher_text:
        if c.isalpha():
            base = "a" if c.islower() else "A"
            plain_text += chr((ord(c) - ord(base) + keys[key_index]) % 26 + ord(base))
            key_index = (key_index + 1) % len(keys)
        else:
            plain_text += c

    print(plain_text)


if __name__ == "__main__":
    main()
