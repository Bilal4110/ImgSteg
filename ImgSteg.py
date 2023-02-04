import cv2
import numpy as np


def binary_converter(
        content):  # This function will be used to convert image pixels and the encoded message into their binary equivalent
    if type(content) == str:
        return ''.join([format(ord(i), "08b") for i in content])

    elif type(content) == bytes or type(content) == np.ndarray:
        return [format(i, "08b") for i in content]

    elif type(content) == int or type(content) == np.uint8:
        return format(content, "08b")
    else:
        print("input not supported, please try again")


class ImgSteg:
    fileName = input("\nImage Filename with extension (Please choose PNG images to ensure efficiency): ")
    img = cv2.imread(fileName)
    encodeMessage = input("Encoded Message:")

    def encoder(self, img, hiddenMessage):
        maximumBytes = img.size // 8
        print(f"You have a maximum of {maximumBytes} bytes to encode...")

        # The below check ensures that the image has enough space to encode the user-supplied message

        if len(hiddenMessage) < maximumBytes:
            print(
                "ERROR: Insufficient space, please increase the size of the image or reduce the message you are trying to encode")

        else:
            # This is the delimiter which will be added to the message. (Any string can be used as a delimiter)
            hiddenMessage += "====="
            binaryMessage = binary_converter(hiddenMessage)
            dataLength = len(binaryMessage)
            index = 0

            for values in img:
                for pixel in values:
                    r, g, b = binary_converter(pixel)
                    if dataLength < index:
