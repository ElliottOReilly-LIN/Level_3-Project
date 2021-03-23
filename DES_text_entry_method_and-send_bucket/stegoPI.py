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
        ascii_value = ord(char)  # Return an integer representing the ASCII value.
        # e.g. ASCII 'a' =  decimal '97' for 0 binary '1 1 0 0 0 0 1'
        for bit_position in range(8):
            power = 7 - bit_position  # Consider this to be 2^7 = from 2^0 or
            # making 2^8 or 256 ie  '0 0 0 0 0 0 0 0'
            # yield is like a return, it is generator and therefore only used once
            yield 1 if ascii_value & (1 << power) else 0  # bitwise left shift operator

# This take a sequence of 'bits' and gives back characters


def chars_provider(pixel_red_values) -> Iterable[str]:
    ascii_value = 0
    # for each 8 bits, it yields one character
    for i, pixel_red_value in enumerate(pixel_red_values):
        ascii_value_bit_position = 7 - i % 8
        if pixel_red_value & 1:
            # Basically, turn back on the bits in the right place
            # this will get back the character embedded
            # if it equal to one, then left shift
            ascii_value |= 1 << ascii_value_bit_position
        if ascii_value_bit_position == 0:
            # 'cha()'' the inverse of 'ord()' returns a string 'a' from '97'
            char: str = chr(ascii_value)
            # just check we are returning a characters until the end
            # otherwise, we are done and can return
            if not char.isprintable() and char != '\n':
                return
            # again, yield is generator and only needed once
            yield char  # giving back a characters, like a return

            ascii_value = 0


''' This function takes in the original image to embed the secret message
    or file into. It also takes in the message string and outputs 
    final stego image, which should look identical'''


def create_image(message: str, input_filename, output_filename: str) -> None:
    img = Image.open(input_filename)
    pixels = np.array(img)  # create an array of pixels from the image
    img.close()
    clear_low_order_bits(pixels)  # Turns off the low order bit, the of
    # bits_provider returns the bits from the message or file one by one
    for i, bit in enumerate(bits_provider(message)):
        # will grab the position of the bit and it's value, i.e. 0 or 1
        row = i // pixels.shape[1]  # fill the rows element with binary 1's
        col = i % pixels.shape[1]  # fill the columns element with binary 1's
        pixels[row, col, 0] |= bit  # the current red value pixel
    out_img = Image.fromarray(pixels)  # create the  secret image form pixel array
    out_img.save(output_filename)
    out_img.close()

# Sets all low end bits to zero ready for manipulation
# This basically turns off the low order bit.


def clear_low_order_bits(pixels) -> None:
    for row in range(pixels.shape[0]):
        for col in range(pixels.shape[1]):
            # use the bitwise 'AND operator' and 'negate' operator
            pixels[row, col, 0] &= ~1  # 'flip' the bit using the '~'
            # one's compliment operator

# Simple function return the original secret message, or file
# This function is only grabbing the RED values from the image,
# as these contain our encode image


def decode_image(filename: str) -> str:
    img = Image.open(filename)
    # Concatenate the string with 'join'
    result = ''.join(chars_provider(img.getdata(band=0)))
    img.close()
    return result
