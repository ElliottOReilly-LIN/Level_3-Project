# Print out the original secret message, or file
from stegoPI import decode_image


def decodeImage():
    decoded = decode_image('secret-stego_image.png')
    # "utf-8"
    print("Decoded: \nThe file you embeded was \n\n" + decoded)
