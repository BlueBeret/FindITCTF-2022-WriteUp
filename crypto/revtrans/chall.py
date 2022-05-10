flag = '123412341234'

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]


enc = 'eiluFIFatv_{Tiy_esyCn}y_ooTd'


def decrypt(ct):
   x = ''
   for j in range(7):
      for i in range(j, len(ct), 7):
         x += ct[i]

   parts = split_len(x[::-1], 4)
   for i in parts:
      print(i[::-1], end="")

decrypt(enc)
