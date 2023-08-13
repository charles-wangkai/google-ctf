def swap_columns(grid, c1, c2):
    for line in grid:
        line[c1], line[c2] = line[c2], line[c1]


def main():
    cipher_text = "rsâ£râ£enigmâ£â£aierheâ£iâ£gluucsclhetersntiâ£aâ£rlaâ£tâ£riayrgpetaiâ£diuâ£Fawhiho}sipatfyâ£ihrâ£aâ£rfaâ£pesâ£etohwreaâ£octtoneeâ£eihetTpxcdeghiâ£roâ£pedâ£yGaledemXToneepetlhtseghectnatanstâ£ripctiharaicsâ£foarsceeâ£ebrnâ£teâ£doemrrâ£c__ltcsaicsaâ£cooâ£wbrnâ£â£aranmeibti,haarhra,sipkltiâ£ci.ctstâ£aâ£lxtcnaenlkLeoakelXpohryâ£patakrntdâ£cilxsUâ£ineheâ£cwthersâ£rpoâ£narahhtrâ£aienlsrtrrâ£o.{rd___nXntiâ£â£ornrtoyrgoorsâ£te.ksipâ£â£crsâ£â£câ£pohelhgctnâ£ieâ£erntatecgâ£teeeAsuvesuX"

    row = 71
    col = 6
    grid = [["." for _ in range(col)] for _ in range(row)]
    r = 0
    c = 0
    for ch in cipher_text.replace("â£", " "):
        grid[r][c] = ch

        r += 1
        if r == row:
            r = 0
            c += 1

    swap_columns(grid, 0, 2)
    swap_columns(grid, 1, 2)
    swap_columns(grid, 2, 3)
    swap_columns(grid, 3, 5)
    swap_columns(grid, 4, 5)

    print("".join("".join(line) for line in grid))


if __name__ == "__main__":
    main()
