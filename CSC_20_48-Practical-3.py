def caesar(text, key, encrypt=True):
    result = ""
    key = key if encrypt else -key
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            end = (ord(char) - start + key) % 26 + start
            result += chr(end)
        else:
            result += char
    return result

if __name__ == "__main__":
    # Caesar Cipher
    plain_text = input("Enter the plain text: ")
    key = int(input("Enter the key: "))
    cipher_text = caesar(plain_text, key)
    print("Cipher Text: ", cipher_text)
    decipher_text = caesar(cipher_text, key, encrypt=False)
    print("Deciphered Text: ", decipher_text)
