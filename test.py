from file import encrypt_vigenere, decrypt_vigenere


with open ("result.txt", "w") as f:
    cases1 = [
            ("PYTHON", "A", "PYTHON"),
            ("python", "a", "python"),
            ("introduction to python", "lsci", "tfvzzvwkeaqv lq aqvpzf"),
            ("ATTACKATDAWN", "LEMON", "LXFOPVEFRNHR"),
        ]
    for i, (plaintext, keyword, chiphertext) in enumerate(cases1):
        if chiphertext == encrypt_vigenere(plaintext, keyword):
            f.write("Test completed" + "\n")
        else:
            f.write("test failed" + "\n")

    cases2 = [
            ("PYTHON", "A", "PYTHON"),
            ("python", "a", "python"),
            ("tfvzzvwkeaqv lq aqvpzf", "lsci", "introduction to python"),
            ("LXFOPVEFRNHR", "LEMON", "ATTACKATDAWN"),
        ]
    for i, (chiphertext, keyword, plaintext) in enumerate(cases2):
        if chiphertext == decrypt_vigenere(plaintext, keyword):
            f.write("Test completed" + "\n")
        else:
            f.write("Test failed" + "\n")
    