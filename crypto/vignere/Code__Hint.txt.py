# Hint: vigorous and sincere. 45 5A 43 52 59 50 54 4F.
# Code: XGQLYGMOZHIVLTKSID
# Note: Masukkan jawaban yang ditemukan ke dalam format flag CTF Find IT untuk mendapatkan flag seutuhnya.

def dekrip(ct, key):
    return("" . join([chr((ord(ct[i])-ord(key[i%len(key)]) + 26) % 26 + ord('A')) for i in range(len(ct))]))

key = "".join(chr(int(x,16)) for x in "45 5A 43 52 59 50 54 4F".split(' '))
cipher = "XGQLYGMOZHIVLTKSID"

print('FindITCTF{' + dekrip(cipher, key) + '}')