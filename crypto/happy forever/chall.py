from secret import HAPPY_NUM, FLAG
import base64

FLAGenc = FLAG[::-1].encode().hex()
ciphertext = [(ord(c)^(HAPPY_NUM[i]+i)) for i,c in enumerate(FLAGenc)]

print(f"ciphertext = {ciphertext}")