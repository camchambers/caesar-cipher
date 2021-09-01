def encrypt(plaintext, offset):
    # Iterate over each character in the plaintext string
    cipher = ""
    for c in plaintext:
        # Convert the character at index c to a numeric Unicode value
        o = ord(c)
        # Increment the integer value at index c by the offset
        o = o + offset
        cipher = cipher + chr(o)
    return cipher


def main():
    print("\nCaesar Cipher\n")
    plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    offset = 1
    print("Plaintext: {}".format(plaintext))
    print("Offset: {}".format(offset))

    ciphertext = encrypt(plaintext, offset)
    print(ciphertext)


if __name__ == '__main__':
    main()
