# Grab image function from
from stegoPI import create_image


def msgEncode():
    # Grab the ciphertext generated from OpenSSL
    with open("RSABase64Cipher") as f:
        line = f.read()

    print("Stega text hidden in lion.png image was: ", line)
    create_image(line, 'lion.png', 'secret-stego_image.png')

