from Crypto.Util.number import long_to_bytes, inverse

N = #
e_1 = #
e_2 = #
enc_key_1_hex = ""
enc_key_2_hex = ""

enc_key_1 = int(enc_key_1_hex, 16)
enc_key_2 = int(enc_key_2_hex, 16)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def recover_key(ct_1, ct_2, e_1, e_2, N):
    gcd, a, b = extended_gcd(e_1, e_2)
    if gcd != 1:
        raise ValueError("e_1 and e_2 are not coprime")
    
    if a < 0:
        ct_1 = inverse(ct_1, N)
        a = -a
    if b < 0:
        ct_2 = inverse(ct_2, N)
        b = -b
    
    pt = (pow(ct_1, a, N) * pow(ct_2, b, N)) % N
    return long_to_bytes(pt)

decrypted_key = recover_key(enc_key_1, enc_key_2, e_1, e_2, N)
print(f"Recovered Encryption Key: {decrypted_key}")

##################################################################
#Расширенный алгоритм Евклида: Функция extended_gcd вычисляет коэффициенты a и b, которые удовлетворяют уравнению a*e1+b*e2=1
#Комбинирование зашифрованных текстов: Если коэффициенты a и b отрицательные, мы берем обратный элемент по модулю N для соответствующих зашифрованных текстов. 
#Затем, используя эти коэффициенты, мы вычисляем исходный текст (ключ шифрования).
