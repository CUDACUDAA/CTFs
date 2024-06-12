from binascii import unhexlify

# Provided data
secret_msg_hex = ''
known_plaintext = '00000000000000000000000000000000'
known_ciphertext_hex = ''

# Convert from hex to bytes
secret_msg_bytes = unhexlify(secret_msg_hex)
known_ciphertext_bytes = unhexlify(known_ciphertext_hex)
known_plaintext_bytes = known_plaintext.encode()

# Deduce keystream
keystream = bytes([kc ^ kp for kc, kp in zip(known_ciphertext_bytes, known_plaintext_bytes)])

# Decrypt the secret message
decrypted_secret_msg_bytes = bytes([sc ^ ks for sc, ks in zip(secret_msg_bytes, keystream)])

print(decrypted_secret_msg_bytes)
