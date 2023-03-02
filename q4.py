def monoalphabetic_substitution(text, key, encrypt=True):
    # Create a dictionary to map characters to their corresponding key values
    key_dict = dict(zip(key, range(len(key))))

    # Inverse key dictionary for decryption
    inv_key_dict = dict(zip(range(len(key)), key))

    result = ""
    for char in text:
        if char.isalpha():
            if encrypt:
                result += key_dict[char.lower()].upper() if char.isupper() else key_dict[char]
            else:
                result += inv_key_dict[char.lower()].upper() if char.isupper() else inv_key_dict[char]
        else:
            result += char
    return result

def polyalphabetic_substitution(text, key, encrypt=True):
    # Create a list of keys 
    key_list = [key[i % len(key)] for i in range(len(text))]

    # Create a dictionary 
    key_dict = dict(zip(key, range(len(key))))

    # Inverse key dictionary for decryption
    inv_key_dict = dict(zip(range(len(key)), key))

    result = ""
    for i, char in enumerate(text):
        if char.isalpha():
            if encrypt:
                result += inv_key_dict[(key_dict[char.lower()] + key_dict[key_list[i].lower()]) % len(key)].upper() if char.isupper() else inv_key_dict[(key_dict[char] + key_dict[key_list[i]]) % len(key)]
            else:
                result += inv_key_dict[(key_dict[char.lower()] - key_dict[key_list[i].lower()]) % len(key)].upper() if char.isupper() else inv_key_dict[(key_dict[char] - key_dict[key_list[i]]) % len(key)]
        else:
            result += char
    return result

if __name__ == "__main__":
    # Monoalphabetic Substitution Cipher
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    cipher_text = monoalphabetic_substitution(plain_text, key)
    print("Cipher Text: ", cipher_text)
    decipher_text = monoalphabetic_substitution(cipher_text, key, encrypt=False)
    print("Deciphered Text: ", decipher_text)

    # Polyalphabetic Substitution Cipher
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    cipher_text = polyalphabetic_substitution(plain_text, key)
    print("Cipher Text: ", cipher_text)
    decipher_text = polyalphabetic_substitution(cipher_text, key, encrypt=False)
    print("Deciphered Text: ", decipher_text)
