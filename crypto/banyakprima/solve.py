from Crypto.Util.number import *
import gmpy2
from output import n,e,c

def nextPrime(prime):
    if isPrime(prime):
        return prime
    else:
        return nextPrime(prime+1)
 
def getN(p):
    q = nextPrime(7*p)
    r = nextPrime(p*q)
    s = nextPrime(q*r)
    return p*q*r*s
 
def find_p(p_guess,n):
    while True:
        n_guess = getN(p_guess)
        if n < n_guess:
            p_guess = p_guess - 2
        elif n > n_guess:
            p_guess = p_guess + 2
        else:
            assert (n == n_guess)
            return p_guess

guess = gmpy2.iroot(n//(7**4),7)[0]
guess += 1
# memastikan kalo guess adalah bilangan ganjil
assert(guess%2 == 1)
p = find_p(guess,n); q = nextPrime(7*p)
r = nextPrime(p*q); s = nextPrime(q*r)
phi = (p-1)*(q-1)*(r-1)*(s-1)
d = inverse(e,phi)
print(long_to_bytes(pow(c,d,n)))
