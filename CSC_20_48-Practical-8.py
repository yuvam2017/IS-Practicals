import numpy as np

def mod_inv(a, m):
    """
    Returns modular inverse of a mod m
    """
    for i in range(1, m):
        if (a*i) % m == 1:
            return i
    return None

def prepare_plaintext(plaintext, n):
    """
    Adds padding to the plaintext if its length is not a multiple of n
    """
    if len(plaintext) % n != 0:
        padding_len = n - (len(plaintext) % n)
        plaintext += "X" * padding_len
    return plaintext

def hill_cipher(key, plaintext):
    """
    Encrypts plaintext using Hill cipher with given key
    """
    n = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(c) - 65 for c in key]).reshape(n, n)
    plaintext = prepare_plaintext(plaintext, n)
    
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = np.array([ord(c) - 65 for c in plaintext[i:i+n]]).reshape(n, 1)
        cipher_block = (key_matrix @ block) % 26
        cipher_text = "".join([chr(c + 65) for c in cipher_block])
        ciphertext += cipher_text
    
    return ciphertext

def hill_decipher(key, ciphertext):
    """
    Decrypts ciphertext using Hill cipher with given key
    """
    n = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(c) - 65 for c in key]).reshape(n, n)
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inv(det, 26)
    if det_inv is None:
        return "Error: determinant has no modular inverse"
    
    key_matrix_inv = (det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 26
    
    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = np.array([ord(c) - 65 for c in ciphertext[i:i+n]]).reshape(n, 1)
        plain_block = (key_matrix_inv @ block) % 26
        plain_text = "".join([chr(c + 65) for c in plain_block])
        plaintext += plain_text
    
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")
    ciphertext = hill_cipher(key, plaintext)
    print("Ciphertext:", ciphertext)
    plaintext = hill_decipher(key, ciphertext)
    print("Decrypted plaintext:", plaintext)
