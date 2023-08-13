def main():
    cipher_text = """\
PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU.
PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV.

AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V.

EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP.

ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}
"""

    plain_text = cipher_text.translate(
        {
            ord("A"): "F",
            ord("B"): "C",
            ord("C"): "K",
            ord("D"): "H",
            ord("E"): "O",
            ord("F"): "S",
            ord("G"): "M",
            ord("H"): "Y",
            ord("I"): "B",
            ord("J"): "V",
            ord("K"): "Q",
            ord("L"): "U",
            ord("M"): "P",
            ord("N"): "L",
            ord("O"): "R",
            ord("P"): "T",
            ord("Q"): "N",
            ord("R"): "I",
            ord("S"): "A",
            ord("T"): "J",
            ord("U"): "G",
            ord("V"): "E",
            ord("W"): "Z",
            ord("X"): "W",
            ord("Y"): "X",
            ord("Z"): "D",
        }
    )

    print(plain_text)


if __name__ == "__main__":
    main()
