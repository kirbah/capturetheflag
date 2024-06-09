def substitute_cipher(text):
    """Substitute characters to decrypt."""
    cipher = "PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU"
    plaint = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    result = ""
    for char in text:
        if char.isalpha():
            result += plaint[cipher.index(char)]
        else:
            result += char
    return result


def find_flag(text):
    """Searches for 'FLAG' in the text (case-insensitive)."""
    return "FLAG" in text.upper()


encrypted_text = """PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU.
PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV.

AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V.

EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP.

ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}"""

decrypted_text = substitute_cipher(encrypted_text)
if find_flag(decrypted_text):
    print(decrypted_text)
else:
    print("FLAG not found after.")
