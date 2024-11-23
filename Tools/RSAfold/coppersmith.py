from sage.all import *
from Crypto.Util.number import long_to_bytes

# Given values
n = 5113166966960118603250666870544315753374750136060769465485822149528706374700934720443689630473991177661169179462100732951725871457633686010946951736764639
c = 329402637167950119278220170950190680807120980712143610290182242567212843996710001488280098771626903975534140478814872389359418514658167263670496584963653
cor_m = 724154397787031699242933363312913323086319394176220093419616667612889538090840511507392245976984201647543870740055095781645802588721

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
