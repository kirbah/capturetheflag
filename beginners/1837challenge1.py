import re

MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '.. .': 'C',
    '-..': 'D',
    '.': 'E',
    '.-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '-.-.': 'J',
    '-.-': 'K',
    '⸺': 'L',
    '--': 'M',
    '-.': 'N',
    '. .': 'O',
    '.....': 'P',
    '..-.': 'Q',
    '. ..': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '.-..': 'X',
    '.. ..': 'Y',
    '... .': 'Z',
    '⸻': '0',
    '.--.': '1',
    '..-..': '2',
    '...-.': '3',
    '....-': '4',
    '---': '5',
    '......': '6',
    '--..': '7',
    '-....': '8',
    '-..-': '9',
    '/': ' ',  # space separator for words
    '{': '{',  # special characters
    '}': '}'
}


def decode_morse(morse_code):
    """Decodes Morse code string into plain text."""
    result = ""
    for code_long in morse_code.split('  '):
        code = code_long.strip()
        if code in MORSE_CODE:
            result += MORSE_CODE[code]
    return result


def vigenere_cipher(text):
    """Shifts characters in text by the given amount."""
    password = "MANCHESTERBLUFFCOMPLETEVICTORY"
    index = 0
    result = ""
    for char in text:
        if char.isalpha():
            # Shift only alphabetical characters
            key_shift = ord(password[index % len(password)]) - ord('A')
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base - key_shift) % 26 + base)
            result += new_char
            index += 1
        else:
            result += char
    return result


with open('1837challenge1.txt', 'rb') as f:
    text = f.read().decode('utf-8')
# add spaces around {} chars
morse_text = re.sub(r'([/{}])', r'  \1  ', text)

decoded_text = decode_morse(morse_text)
print(decoded_text)
crypted = decoded_text[decoded_text.find('{') + 1: decoded_text.find('}')]
print(f"Crypted: {crypted}")
decrypt = vigenere_cipher(crypted)
print(f"Decrypt: {decrypt}")
