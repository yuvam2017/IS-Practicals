def encrypt(message, shift):
    """
    Encrypts a message using the Caesar Cipher with the specified shift value.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Determine the ASCII value of the character
            ascii_value = ord(char)
            # Determine the new ASCII value by adding the shift value
            new_ascii_value = ascii_value + shift
            # If the new ASCII value is outside the range of letters, wrap around
            if char.isupper():
                if new_ascii_value > ord('Z'):
                    new_ascii_value -= 26
                elif new_ascii_value < ord('A'):
                    new_ascii_value += 26
            else:
                if new_ascii_value > ord('z'):
                    new_ascii_value -= 26
                elif new_ascii_value < ord('a'):
                    new_ascii_value += 26
            
            # Convert the new ASCII value back to a character and add it to the encrypted message
            encrypted_char = chr(new_ascii_value)
            encrypted_message += encrypted_char
        else:
            
            # If the character is not a letter, add it to the encrypted message unchanged
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)
