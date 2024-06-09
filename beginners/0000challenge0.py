def caesar_cipher(text, shift):
  """Shifts characters in text by the given amount."""
  result = ""
  for char in text:
    if char.isalpha():
      # Shift only alphabetical characters
      base = ord('a') if char.islower() else ord('A')
      new_char = chr((ord(char) - base + shift) % 26 + base)
      result += new_char
    else:
      result += char
  return result

def find_flag(text):
  """Searches for 'FLAG' in the text (case-insensitive)."""
  return "FLAG" in text.upper()

text = """Naljnl, Pnrfne jnf n fxvyyrq pbzzhavpngbe, naq ur hfrq n inevrgl bs zrgubqf gb xrrc uvf zrffntrf frperg sebz uvf rarzvrf.
Bar bs gurfr zrgubqf jnf gur Pnrfne pvcure, n fvzcyr grpuavdhr gb boshfpngr pbzzhavpngvbaf. SYNT{ebgngr_gung_nycunorg}"""
max_iterations = 27

for i in range(max_iterations):
  shifted_text = caesar_cipher(text, i)
  if find_flag(shifted_text):
    print(f"Found FLAG after {i} shifts:\n{shifted_text}")
    break
else:
  print("FLAG not found after", max_iterations, "iterations.")
