def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Shift character by the specified amount
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            ciphertext += shifted_char
        else:
            # If the character is not an alphabet, leave it unchanged
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

# Example usage:
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift = 3
    encrypted_text = caesar_cipher_encrypt(plaintext, shift)
    print("Encrypted:", encrypted_text)
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
    print("Decrypted:", decrypted_text)
