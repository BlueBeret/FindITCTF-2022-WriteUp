from Crypto.Util.number import getPrime, bytes_to_long
from secret import FLAG, e

m = bytes_to_long(FLAG)
modulos = []
ciphertexts = []

for i in range(1,e+1):
    p = getPrime(256)
    q = getPrime(256)

    N = p*q

    print(f"n_{i} = {N}, c_{i} = {pow(m, e, N)}")
    modulos.append(N)
    ciphertexts.append(pow(m, e, N))