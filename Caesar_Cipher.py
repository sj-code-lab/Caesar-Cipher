# Caesar Cipher
def caesar(text, shift, encrypt=True):
    # Validate that the shift value is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Ensure the shift is within the valid Caesar cipher range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # Define the alphabet used for translation
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Reverse the shift when decrypting
    if not encrypt:
        shift = -shift
    
    # Create the shifted alphabet (e.g., shift=3 → 'def...abc')
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Build a translation table for both lowercase and uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text using the Caesar cipher mapping
    return text.translate(translation_table)


def encrypt(text, shift):
    # Wrapper function for encryption
    return caesar(text, shift)
    
def decrypt(text, shift):
    # Wrapper function for decryption
    return caesar(text, shift, encrypt=False)


# Example encrypted message
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

# Decrypt using a shift of 13 (ROT13)
decrypted_text = decrypt(encrypted_text, 13)

print(decrypted_text)
