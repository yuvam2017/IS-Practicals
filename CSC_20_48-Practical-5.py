def playfair_cipher(key, message, encrypt=True):
    key = key.replace(" ", "").upper()
    message = message.replace(" ", "").upper()

    # Generate the Playfair square
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    square = ""
    for letter in key:
        if letter not in square:
            square += letter
    for letter in alphabet:
        if letter not in square:
            square += letter

    # Apply the Playfair cipher
    pairs = []
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        if len(pair) == 1:
            pair += "X"
        pairs.append(pair)

    cipher_text = ""
    for pair in pairs:
        row1, col1 = divmod(square.index(pair[0]), 5)
        row2, col2 = divmod(square.index(pair[1]), 5)

        if row1 == row2:
            cipher_text += square[row1*5+(col1+1)%5]
            cipher_text += square[row2*5+(col2+1)%5]
        elif col1 == col2:
            cipher_text += square[((row1+1)%5)*5+col1]
            cipher_text += square[((row2+1)%5)*5+col2]
        else:
            cipher_text += square[row1*5+col2]
            cipher_text += square[row2*5+col1]

    # Decrypt
    if not encrypt:
        plain_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = divmod(square.index(pair[0]), 5)
            row2, col2 = divmod(square.index(pair[1]), 5)

            if row1 == row2:
                plain_text += square[row1*5+(col1-1)%5]
                plain_text += square[row2*5+(col2-1)%5]
            elif col1 == col2:
                plain_text += square[((row1-1)%5)*5+col1]
                plain_text += square[((row2-1)%5)*5+col2]
            else:
                plain_text += square[row1*5+col2]
                plain_text += square[row2*5+col1]

        return plain_text.replace("X", "")

    return cipher_text

if __name__ == "__main__":
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    encoded_text = playfair_cipher(key,message,encrypt=True)
    print("Cipher Text:",encoded_text)
    decoded_text = playfair_cipher(key,message,encrypt=False)
    print("Plain Text:", decoded_text)
