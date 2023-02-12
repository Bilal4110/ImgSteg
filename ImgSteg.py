import cv2
import numpy as np


class ImgSteg:



    def open_image(self, img):

        """

        This function opens and displays an image using the OpenCV module.

        :parameter:

        img: This is the path of the image to be opened. This will be supplied by a user via an input.

        :return:

        image: Returns the data of the opened image in the form of a numpy array.

        """

        image = cv2.imread(img, cv2.IMREAD_ANYCOLOR)
        cv2.imshow("Your Inputted image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return image

    def binary_converter(self, content):
        """

        Converts a string (Binary message) or a numpy array (pixel) to its equivalent binary representation

        :parameter:

         content: the inputted content which needs to be converted to binary.

        :return:

        If the content is string, then a binary string is returned.
        If the content is a numpy ndarray, then a list of binary pixel values is returned.

        """

        if type(content) == str:
            return ''.join([format(ord(i), "08b") for i in
                            content])  # https://www.geeksforgeeks.org/python-convert-string-to-binary/
        elif type(content) == np.ndarray:
            return [format(i, "08b") for i in content]  # https://docs.replit.com/tutorials/python/steganography

    def hide_text(self, image, hiddenMessage):

        """
        This function find the total size of an image (totalPixels).
        :param image:
        :param hiddenMessage:
        :return:


        :References:
        https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372 -


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


    def encoder(self):
        fileName = input("choose an image: ")
        if fileName.endswith(".png"):
            img = self.open_image(fileName)
            encodeMessage = input("choose message: ")

            if len(encodeMessage) == 0:
                print("\nERROR: Please add a message to encode!")



if __name__ == "__main__":
    obj = ImgSteg()
    obj.encoder()
