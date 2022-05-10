known = "FindITCTF"
# suka makan 10 pies pertama, coba hitung knownflag juga ternyata ada 10

with open('./crypto/asciipi/Code.txt', 'r') as f:
    num = [int(i) for i in f.readlines()]
pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
pi = [int(i) for i in pi[:10]]
for i,j in enumerate(num):
    divisor = pi[i%10]
    print(chr(j//divisor), end="")    
