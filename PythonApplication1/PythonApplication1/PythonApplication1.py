def MaHoa(plaintext, key):
    ciphertext = ""
    key = key % 26
    for c in plaintext:
        if c.isupper():
            so = ord(c) - 65
            so = (so + key) % 26
            ciphertext += chr(so + 65)
        elif c.islower():
            so = ord(c) - 97
            so = (so + key) % 26
            ciphertext += chr(so + 97)
        else:
            ciphertext += c
    return ciphertext

p = "LeHongTham"   
key = 32          
c = MaHoa(p, key)
print("Plaintext :", p)
print("Ciphertext:", c)

