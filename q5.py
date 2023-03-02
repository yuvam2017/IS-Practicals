def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key_chars = sorted(set(key), key=key.index)
    
    remaining_chars = [chr(i+65) for i in range(26) if chr(i+65) not in key_chars and chr(i+65) != "J"]
    key_chars += remaining_chars
   
    matrix = [key_chars[i:i+5] for i in range(0, 25, 5)]
    return matrix

def playfair(text, key, encrypt=True):
    # Generate the key matrix
    matrix = generate_key_matrix(key)
    
    text = text.replace(" ", "").upper().replace("J", "I")
    text_pairs = [text[i:i+2] for i in range(0, len(text), 2)]
   
    # Encrypt/Decrypt the pairs
    result = ""
    for pair in text_pairs:
        if len(pair) == 2:
            x1, y1 = divmod(matrix.index([char for char in pair][0]), 5)
            x2, y2 = divmod(matrix.index([char for char in pair][1]), 5)
            if x1 == x2:
                # Same row
                y1 = (y1 + 1) % 5 if encrypt else (y1 - 1) % 5
                y2 = (y2 + 1) % 5 if encrypt else (y2 - 1) % 5
            elif y1 == y2:
                # Same column
                x1 = (x1 + 1) % 5 if encrypt else (x1 - 1) % 5
                x2 = (x2 + 1) % 5 if encrypt else (x2 - 1) % 5
            else:
                # Rectangle
                y1, y2 = y2, y1
            result += matrix[x1][y1] + matrix[x2][y2]
    return result

if __name__ == "__main__":
    # Playfair Cipher
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")
    cipher_text = playfair(plain_text, key)
    print("Cipher Text: ", cipher_text)
    decipher_text = playfair(cipher_text, key, encrypt=False)
    print("Deciphered Text: ", decipher_text)
