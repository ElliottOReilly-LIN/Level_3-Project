from stegapy import create_image
import subprocess

    with open("plaintext.csv") as f:
        line = f.read() + '\n'  # add trailing new line character

    # Grab image function from
    # file = open("plaintext-CSV.txt")
    # line = file.read().replace("\n", " ")
    # Show the contents of PDF file
    # print(line)
    # file.close()

    # print(pt)
    # line = '''Steganography is the practice of concealing a file,
    # message, image, or video within another file,
    # The word Steganography combines the Greek words
    # steganos, meaning "covered or concealed", and graphe meaning
    # "writing". To wit, I am endeavoring to understand this guys code'''
    create_image(line, 'lion.png', 'secretXXX-Lion-image.png')
