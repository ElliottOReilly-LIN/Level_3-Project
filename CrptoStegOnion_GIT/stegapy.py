''' Program that embeds a secret message or a given media format.
in a .png image. Original source code from: Dave Briccetti - GitHub'''

from typing import Iterable
import numpy as np
from PIL import Image

# Grab the individual chars from the input string,
# and set an ASCII value for each bit

# -> Iterable Tells the function to return an integer. although its not forced
def bits_provider(message) -> Iterable[int]:
    for char in message:
        ascii_value = ord(char)  # Return an integer representing the ASCII value. e.g. 'a' = 97
        for bit_position in range(8):
            power = 7 - bit_position
            # yield is like a return, it is generator and therefore only used once
            yield 1 if ascii_value & (1 << power) else 0  # bitwise left shift operator


def chars_provider(pixel_red_values) -> Iterable[str]:
    ascii_value = 0
    for i, pixel_red_value in enumerate(pixel_red_values):
        ascii_value_bit_position = 7 - i % 8
        if pixel_red_value & 1:
            ascii_value |= 1 << ascii_value_bit_position
        if ascii_value_bit_position == 0:
            char: str = chr(ascii_value)  # the inverse of 'ord()' returns a string 'a' from '97'
            if not char.isprintable() and char != '\n':
                return
            # again, yield is generator and only needed once
            yield char

            ascii_value = 0

''' This function takes in the original image to embed the secret message
    or file into. It also takes in the message string and outputs 
    final stego image, which should look identical'''
def create_image(message: str, input_filename, output_filename: str) -> None:
    img = Image.open(input_filename)
    pixels = np.array(img)
    img.close()
    clear_low_order_bits(pixels)
    for i, bit in enumerate(bits_provider(message)):
        row = i // pixels.shape[1]
        col = i % pixels.shape[1]
        pixels[row, col, 0] |= bit
    out_img = Image.fromarray(pixels)
    out_img.save(output_filename)
    out_img.close()

# Sets all low end bits to zero ready for manipulation
def clear_low_order_bits(pixels) -> None:
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            pixels[row, col, 0] &= ~1  # 'flip' the bit using the '~' compliment operator

# Simple function return the original secret message, or file
def decode_image(filename: str) -> str:
    img = Image.open(filename)
    # Concatenate the string with 'join'
    result = ''.join(chars_provider(img.getdata(band=0)))
    img.close()
    return result
