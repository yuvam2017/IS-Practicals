def rail_fence_encrypt(message, key):
    rail_fence = [[] for i in range(key)]
    fence_direction = 1
    fence_position = 0
    
    for letter in message:
        rail_fence[fence_position].append(letter)
        fence_position += fence_direction
        
        if fence_position == 0 or fence_position == key - 1:
            fence_direction = -fence_direction
            
    cipher_text = ''
    
    for rail in rail_fence:
        cipher_text += ''.join(rail)
        
    return cipher_text

def rail_fence_decrypt(cipher_text, key):
    rail_fence = [[] for i in range(key)]
    fence_direction = 1
    fence_position = 0
    cipher_index = 0
    
    for i in range(len(cipher_text)):
        rail_fence[fence_position].append(None)
        fence_position += fence_direction
        
        if fence_position == 0 or fence_position == key - 1:
            fence_direction = -fence_direction
            
    for rail in rail_fence:
        for i in range(len(rail)):
            rail[i] = cipher_text[cipher_index]
            cipher_index += 1
            
    fence_direction = 1
    fence_position = 0
    plain_text = ''
    
    for i in range(len(cipher_text)):
        plain_text += rail_fence[fence_position][0]
        del rail_fence[fence_position][0]
        fence_position += fence_direction
        
        if fence_position == 0 or fence_position == key - 1:
            fence_direction = -fence_direction
            
    return plain_text

if __name__ == '__main__':
    message = input("Enter the message : ")
    key = int(input("Enter the key : "))
    encrypted_message = rail_fence_encrypt(message, key)
    decrypted_message = rail_fence_decrypt(encrypted_message, key)
    print(f'Original message: {message}')
    print(f'Encrypted message: {encrypted_message}')
    print(f'Decrypted message: {decrypted_message}')
