def vigenere_cipher(text):
  """Shifts characters in text by the given amount."""
  password = "caesar"
  index = 0
  result = ""
  for char in text:
    if char.isalpha():
      # Shift only alphabetical characters
      key_shift = ord(password[index % len(password)]) - ord('a')
      base = ord('a') if char.islower() else ord('A')
      new_char = chr((ord(char) - base - key_shift) % 26 + base)
      result += new_char
      index += 1
    else:
      result += char
  return result

def find_flag(text):
  """Searches for 'FLAG' in the text (case-insensitive)."""
  return "FLAG" in text.upper()

encrypted_text = """Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij.
Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}"""

decrypted_text = vigenere_cipher(encrypted_text)
if find_flag(decrypted_text):
  print(decrypted_text)
else:
  print("FLAG not found")
