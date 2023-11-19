def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    while len(keyword) < len(plaintext):
        keyword *= 2
    for i, elem in enumerate(plaintext):
        first_letter = ord("A") if keyword[i].isupper() else ord("a")
        if elem.isalpha() and elem.isupper():
            if keyword[i].isupper():
                num = ord(elem) + (ord(keyword[i]) - first_letter)
            if keyword[i].islower():
                num = ord(elem) + (ord(keyword[i]) - first_letter)
            if num > ord("Z"):
                num = ord("A") + (num - ord("Z")) - 1
            ciphertext += chr(num)
        if elem.isalpha() and elem.islower():
            if keyword[i].isupper():
                num = ord(elem) + (ord(keyword[i]) - first_letter)
            if keyword[i].islower():
                num = ord(elem) + (ord(keyword[i]) - first_letter)
            if num > ord("z"):
                num = ord("a") + (num - ord("z")) - 1
            ciphertext += chr(num)
        if not (elem.isalpha()):
            ciphertext += elem
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    while len(keyword) < len(ciphertext):
        keyword *= 2
    for i in range(len(ciphertext)):
        first_letter = ord("A") if keyword[i].isupper() else ord("a")
        if ciphertext[i].isalpha() and ciphertext[i].isupper():
            if keyword[i].isupper():
                num = ord(ciphertext[i]) - (ord(keyword[i]) - first_letter)
            if keyword[i].islower():
                num = ord(ciphertext[i]) - (ord(keyword[i]) - first_letter)
            if num < ord("A"):
                num = ord("Z") - (ord("A") - num) + 1
            plaintext += chr(num)
        if ciphertext[i].isalpha() and ciphertext[i].islower():
            if keyword[i].isupper():
                num = ord(ciphertext[i]) - (ord(keyword[i]) - first_letter)
            if keyword[i].islower():
                num = ord(ciphertext[i]) - (ord(keyword[i]) - first_letter)
            if num < ord("a"):
                num = ord("z") - (ord("a") - num) + 1
            plaintext += chr(num)
        if not (ciphertext[i].isalpha()):
            plaintext += ciphertext[i]
    return plaintext
