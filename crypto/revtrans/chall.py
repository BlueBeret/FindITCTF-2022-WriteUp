flag = '123412341234'

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
   print(order[1])
   
   print(sorted(order.keys()))

   reversetext =''
   ciphertext = ''
   i=len(plaintext)-1
   while i >= 0:
      reversetext = reversetext + plaintext[i]
      i=i-1
   

   for index in sorted(order.keys()):
      for part in split_len(reversetext, len(key)):
         try:
            ciphertext += part[order[index]]
         except IndexError:
            continue
        
            
   return ciphertext

def decode (key, ciphertext):
   order = {
      int(num): val for num, val in enumerate(key)
   }
   parts = split_len(ciphertext, len(key))

enc = 'eiluFIFatv_{Tiy_esyCn}y_ooTd'
print(len(enc))

while 1:
   x = ''
   for j in range(7):
      for i in range(j, len(enc), 7):
         x += enc[i]

   parts = split_len(x[::-1], 4)
   for i in parts:
      print(i[::-1], end="")

   break
