# Hint: vigorous and sincere. 45 5A 43 52 59 50 54 4F.
# Code: XGQLYGMOZHIVLTKSID
# Note: Masukkan jawaban yang ditemukan ke dalam format flag CTF Find IT untuk mendapatkan flag seutuhnya.

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

key = "".join(chr(int(x,16)) for x in "45 5A 43 52 59 50 54 4F 45 5A 43 52 59 50 54 4F 45 5A 43 52 59 50 54 4F".split(' '))
cipher = "XGQLYGMOZHIVLTKSID"

print(originalText(cipher, key))

print(len('THOUARTAVIGENEREEE'))
print(len(cipher))
b'FindITCTF{THOUARTAVIGENEREEE}' # salah