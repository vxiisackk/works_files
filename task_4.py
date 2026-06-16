f = open("secret.txt", "r", encoding="utf-8")
text = f.read()
f.close()

encrypted = ""
for c in text:
    if c.isalpha():
        if c.islower():
            encrypted += chr((ord(c) - ord('a') + 3) % 26 + ord('a'))
        else:
            encrypted += chr((ord(c) - ord('A') + 3) % 26 + ord('A'))
    else:
        encrypted += c

f = open("encrypted.txt", "w", encoding="utf-8")
f.write(encrypted)
f.close()

f = open("encrypted.txt", "r", encoding="utf-8")
enc = f.read()
f.close()

decrypted = ""
for c in enc:
    if c.isalpha():
        if c.islower():
            decrypted += chr((ord(c) - ord('a') - 3) % 26 + ord('a'))
        else:
            decrypted += chr((ord(c) - ord('A') - 3) % 26 + ord('A'))
    else:
        decrypted += c

f = open("decrypted.txt", "w", encoding="utf-8")
f.write(decrypted)
f.close()
