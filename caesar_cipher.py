# Iterate over each character in the plaintext string.
# Convert the character to a numeric Unicode value.
# Increment the numeric value by the offset.
# Convert the integer back to a character and append to cipher. 
def encrypt(plaintext, offset):
    encrypted = ""
    for c in plaintext:
        encrypted = encrypted + chr(ord(c)+ offset)
    return encrypted


def main():
    print("\nCaesar Cipher\n")
    
    plaintext = "The quick brown fox jumps over the lazy dog."
    print("Plaintext: {}".format(plaintext))

    offset = 1
    print("Offset: {}".format(offset))
    
    ciphertext = encrypt(plaintext, offset)
    print("Ciphertext: {}".format(ciphertext))


if __name__ == '__main__':
    main()
