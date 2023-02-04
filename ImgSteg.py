import cv2
import numpy as np


def binary_converter(content): # This function will be used to convert image pixels and the encoded message into their binary equivalent
    if type(content) == str:
        return ''.join([format(ord(i), "08b") for i in content])

    elif type(content) == bytes or type(content) == np.ndarray:
        return [format(i, "08b") for i in content]

    elif type(content) == int or type(content) == np.uint8:
        return format(content, "08b")
    else:
        print ("input not supported, please try again")


class ImgSteg:
    fileName = input("\nImage Filename with extension (Please choose PNG images to ensure efficiency): ")
    img = cv2.imread(fileName)
    encodeMessage = input("Encoded Message:")

    value = 255
    convertedInt = binary_converter(value)
    print(convertedInt)
    value2 = "HELLO"
    convertedstr = binary_converter(value2)
    print(convertedstr)






