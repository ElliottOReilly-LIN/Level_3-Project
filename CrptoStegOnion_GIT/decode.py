# Print out the original secret message, or file
from stegapy import decode_image

decoded = decode_image('secretXXX-Lion-image.png')
# "utf-8"
print("decoded\n\n" + decoded)
