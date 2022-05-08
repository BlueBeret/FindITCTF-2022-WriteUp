import random,string
import hashlib

flag = "FindITCTF{REDACTED}"
enc_flag = ""
random.seed("FINDIT")
now = ""
ct = []
for c in flag:
  if c.islower():
	  enc_flag += chr((ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
	  enc_flag += chr((ord(c)-ord('A')+random.randrange(0,26))%26 + ord('A'))
  elif c.isdigit():
	  enc_flag += chr((ord(c)-ord('0')+random.randrange(0,10))%10 + ord('0'))
  else:
	  enc_flag += c

for c in enc_flag:
    now += c
    ct.append(
            int(hashlib.sha512(now.encode()).hexdigest(), 16)>>256
        )

print(f"ct = {ct}")