from Crypto.Util.number import inverse

n = 363241
e = 7
p = 449
q = 809
ct = 244800

phi = (p-1)*(q-1)

d = inverse(e,phi)
m = pow(ct,d,n)

m_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
m_str = m_bytes.decode('utf-8')					#use latin-1 if u have probs

print (f'Decimal: {m}')
print (f'Hex : {hex(m)}')
print (f'UTF-8/latin-1 : {m_str}')
