import cv2
import numpy as np


class MyClass:
    fileName = input("\nImage Filename with extension (Please choose PNG images to ensure efficiency): ")
    img = cv2.imread(fileName)

    encodeMessage = input("Encoded Message:")

    def open_image(self):
        if self.fileName.endswith("png") or self.fileName.endswith("jpg") or self.fileName.endswith(
                "jpeg"):  # Check to see if inputted filename is a valid image.
            cv2.imshow('Your inputted image: ', self.img)
            cv2.waitKey(0)
        elif self.fileName == "":
            print("\n ERROR: Can not leave empty")
            quit()
        else:
            print("\nERROR: Please choose a valid image")
            quit()

    def message_to_binary(self):
        if type(self.encodeMessage) == str:
            return ''.join(
                [format(ord(i), "08b") for i in self.encodeMessage])  # Converts the inputted string into binary

        else:
            raise TypeError("Input type not supported")

    def encode(self, secretMessage):
        totalPixels = self.img.shape[0] * self.img[1] * 3 // 8
        print(f"Maximum bytes to encode", totalPixels)
        if len(secretMessage) > totalPixels:
            raise ValueError("Error encountered, please use bigger image or less data")
        secretMessage += "DDDDD" # DELIMITER
        data_index = 0
        binary_Secret_Message = self.message_to_binary(secretMessage)
        data_len


if __name__ == '__main__':
    obj = MyClass()
    obj.open_image()
    obj.message_to_binary()
    obj.encode()
