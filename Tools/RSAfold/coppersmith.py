from sage.all import *
from Crypto.Util.number import long_to_bytes

# Given values
n = 
c = 
cor_m = 

# The random difference r has 160 bits, so the maximum value of r is:
max_r = 2**160

# Define the polynomial
R = PolynomialRing(Zmod(n), 'x')
x = R.gen()
f = (cor_m + x)**2 - c

# Use the Coppersmith method to find small roots of the polynomial
roots = f.small_roots(X=max_r, beta=0.5)

# If we find a valid r, compute m
if roots:
    r = roots[0]
    m = cor_m + int(r)  # Convert Sage integer to Python integer
    plaintext = long_to_bytes(m)
    print("Decrypted message:", plaintext)
else:
    print("No valid root found.")
