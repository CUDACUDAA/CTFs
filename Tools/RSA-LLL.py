from sage.all import *
import binascii

n = #
e = #
c = #

for i in range(100):
    msg = b"plaintext"
    msg += b'\x00'*i
    msg += b'}'
    msg = int(binascii.hexlify(msg), 16)
    P = PolynomialRing(Zmod(n), names=('x',)); (x,) = P._first_ngens(1)
    f = (msg + x)**e - c
    f = f.monic()
    m = f.small_roots(epsilon=1/20)
    if m:
        flag = msg + int(m[0])
        print(flag.to_bytes(100).decode())
        break
