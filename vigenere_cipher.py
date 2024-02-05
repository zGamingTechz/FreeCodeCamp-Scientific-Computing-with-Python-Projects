# A simple vigenere cipher
def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():

        # Append space to the message
        if not char.isalpha():
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text


print("Welcome to Vigenere Cipher!")
while True:
    print("enter 'E' to encrypt")
    print("enter 'D' to decrypt")
    choice = input("Enter 'E' or 'D': ")
    if choice.lower() == 'e':
        text = input("Enter Text to Encrypt: ")
        custom_key = input("Enter Key: ")
        encryption = vigenere(text, custom_key, 1)
        print("Encrypted Text: ", encryption)
    elif choice.lower() == 'd':
        text = input("Enter Text to Decrypt: ")
        custom_key = input("Enter Key: ")
        decryption = vigenere(text, custom_key, -1)
        print("Decrypted Text: ", decryption)
        
