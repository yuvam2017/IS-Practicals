import string

def monoalphabetic_cipher(text, key, encrypt=True):
    
    alphabet = string.ascii_lowercase
    key_dict = dict(zip(alphabet, key))
    inv_key_dict = {v: k for k, v in key_dict.items()}
  
    result = ""
   
    for char in text:
        if char.lower() in alphabet:
            if encrypt:
                result += key_dict[char.lower()].upper() if char.isupper() else key_dict[char]
            else:
                result += inv_key_dict[char.lower()].upper() if char.isupper() else inv_key_dict[char]
        else:
            result += char
    return result

def polyalphabetic_substitution(text, key, encrypt=True):
    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            key_index = i % len(key)
            shift = ord(key[key_index].upper()) - ord('A')
            if encrypt:
                result += chr((ord(char.upper()) + shift - 2*ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char.upper()) - shift - 2*ord('A')) % 26 + ord('A'))
        else:
            result += char
    return result


if __name__ == "__main__":
    print("MONOALPHABETIC CIPHER SUBSTITUTION")
    plaintext = input("Enter the Text : ")
    key = input("Enter the Key (or press Enter for the default key) : ")
    key = "phqgiumeaylnofdxjkrcvstzwb" if key == "" else key
    ciphertext = monoalphabetic_cipher(plaintext, key)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    decrypted_text = monoalphabetic_cipher(ciphertext, key, encrypt=False)
    print("Decrypted text:", decrypted_text)


    print("\n\nPOLYALPHABETIC CIPHER SUBSTITUTION")
    plaintext = input("Enter the Text : ")
    key = input("Enter the Key (or press Enter for the default key) : ")
    key = "losientoadios" if key == "" else key
    ciphertext = polyalphabetic_substitution(plaintext, key)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    decrypted_text = polyalphabetic_substitution(ciphertext, key, encrypt=False)
    print("Decrypted text:", decrypted_text)
