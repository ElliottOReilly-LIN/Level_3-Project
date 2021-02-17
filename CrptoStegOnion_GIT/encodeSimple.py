from google.cloud import storage

# Grab image function from
from stegapy import create_image


def msgEncode():

    # with open("secretMSG.txt") as f:
    #     line = f.read()

    with open("ciphertext.enc", encoding='latin-1') as f:
        line = f.read()
# line = '''Steganography is the practice of concealing a file,
# message, image, or video within another file,
# The word Steganography combines the Greek words
# steganos, meaning "covered or concealed", and graphe meaning
# "writing". To wit, I am endeavoring to understand this guys code'''
    print("Stega text hidden in lion.png image was: ", line)
    create_image(line, 'lion.png', 'secretXXX-Lion-image.png')


# encoding='latin-1'
