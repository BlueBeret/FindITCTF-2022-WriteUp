from Crypto.Util.number import *
import gmpy2
n = 991780332070847898144930172913707154337428968947289369950557418182205916671610439120415358846651351930506089582472303042933616371165128107548726642508866988284488166396083880240510413080431759514941229838260223120292397812794508537379728621988207944460296809293569542376203
e = 65537
c = 0xa42d23224b72bcd5de3712ea6e172eb1e664f3a56d0913b54d53064708a9a7d2d039db467296c41fccdff6ef0ccc6605c2cb6b1a7bff8870a3b8bf2a9a96cba566d2a22c86e5ef25be144856976a7d0c113a54bb187997625c2dee5cdb484a5b43ca6b00df900f580f3d07d50004cd312d

 
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
 
def find_p(papprox,n):
    i = 0
    while True:
        i += 1
        n_approx = getN(papprox)
        if n < n_approx:
            papprox = papprox - 2
            print('0',end="")
        elif n > n_approx:
            papprox = papprox + 2
        else:
            print(i)
            assert (n == n_approx)
            return papprox

p7 = n//(7**4)
papprox = gmpy2.iroot(p7,7)[0]
papprox += 1
assert(papprox%2 == 1)
p = find_p(papprox,n)
q = nextPrime(7*p)
r = nextPrime(p*q)
s = nextPrime(q*r)
phi = (p-1)*(q-1)*(r-1)*(s-1)
d = inverse(e,phi)
pt = long_to_bytes(pow(c,d,n))\

print(pt)
