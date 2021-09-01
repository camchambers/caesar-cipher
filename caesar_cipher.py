import sys

# Iterate over each character in the plaintext string.
# Convert the character to a numeric Unicode value.
# Increment the numeric value by the offset.
# Convert the integer back to a character and append to cipher.


def encrypt(plaintext, offset):
    encrypted = ""
    for c in plaintext:
        encrypted = encrypted + chr(ord(c) + offset)
    return encrypted


def main():
    print("\nCaesar Cipher\n")

    # Validate that 2 arguments are provided to the program.
    if (len(sys.argv) != 3):
        sys.exit(
            "Please provide a plaintext string and a numeric offset as arguments.")

    plaintext = str(sys.argv[1])

    # Validate that the second argument (offset) is numeric.
    if (sys.argv[2].isnumeric()):
        offset = int(sys.argv[2])
    else:
        sys.exit("Please provide a numeric offset as a second argument.")

    print("Plaintext: {}".format(plaintext))

    print("Offset: {}".format(offset))

    ciphertext = encrypt(plaintext, offset)
    print("Ciphertext: {}".format(ciphertext))


if __name__ == '__main__':
    main()
