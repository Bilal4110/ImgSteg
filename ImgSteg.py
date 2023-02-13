import cv2 # OpenCV-Module
import numpy as np


class ImgSteg:

    def open_image(self, img):
        """
        This function opens and displays an image using the OpenCV module.

            :param img: This is the path of the image to be opened. This will be supplied by a user via the terminal.
            :type img: str
            :return image: Returns the data of the opened image in the form of a numpy array.
            :rtype image: numpy.ndarray
        """

        image = cv2.imread(img, cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Your Inputted image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return image

    def binary_converter(self, data):
        """
        Converts a string (Binary message) or a numpy array (pixel) into its equivalent binary value

            :param data: Input data which needs to be converted into binary
            :type data: str or numpy.ndarray
            :return: The binary equivalent of the supplied data
            :rtype: string or list of strings in binary equivalent (Depending on the type of data inputted)
        """

        if type(data) == str:
            return ''.join([format(ord(i), "08b") for i in data])  # https://www.geeksforgeeks.org/python-convert-string-to-binary/
        elif type(data) == np.ndarray: # this is the data in the opened image
            return [format(i, "08b") for i in data]  # https://docs.replit.com/tutorials/python/steganography

    def hide_text(self, image, hiddenMessage):
        """This function hides a text-based message into an image using the LSB method. It first calculates the sizes of both the image and the message (with delimiter) which needs to be encoded.
            This is to ensure that there enough available bytes to encode. If there is enough space, then a message is encoded within the least significant bits of the image's pixels

            :param image: Image which will be used to store the encoded message (Cover Image)
            :param hiddenMessage: Message that will be encoded and hidden into the image. This is to be supplied by the user in the form of an input
            :type image: numpy.ndarray
            :type hiddenMessage: str
            :returns: The modified image data containing the hidden message encoded within its pixels
            :rtype: numpy.ndarray

            References:https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372 - EXPAND!!!
        """

        totalBytes = image.size // 8  # calculates the total size of the image
        print(f"You have a total of {totalBytes} bytes to encode")
        delimiter = "*****"  # This will be useful in the decode section

        if len(hiddenMessage + delimiter) >= totalBytes:
            print("ERROR: Insufficient space, please reduce the size of the message")
            quit()

        else:
            binaryMessage = self.binary_converter(hiddenMessage + delimiter)# Binary equivalent of the both the delimiter and the message to be encoded
            binaryLength = len(binaryMessage)
            checkIndex = 0
            for row in image:
                for pixel in row:
                    r, g, b = self.binary_converter(pixel)
                    for x in range(3):
                        if checkIndex < binaryLength:
                            channel = [r, g, b][x]
                            modifiedLSB = int(channel[:-1] + "0")
                            pixel[x] = modifiedLSB + int(binaryMessage[checkIndex])
                            checkIndex += 1
                    if checkIndex >= binaryLength:
                        break
            return image


    def encode(self):

        fileName = input("choose an image: ")
        if fileName.endswith(".png"):
            img = self.open_image(fileName)
            print(type(img))
            encodeMessage = input("choose message: ")

            if len(encodeMessage) == 0:
                print("\nERROR: Please add a message to encode!")

    def show_text(self, enImg):

        pass



if __name__ == "__main__":
    obj = ImgSteg()
    obj.encode()
