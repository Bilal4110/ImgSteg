import cv2
import numpy as np


class ImgSteg:


    def open_image(self, img):

        """
        This function opens and displays an image in any colour using the OpenCV module.

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
            return ''.join([format(ord(i), "08b") for i in content]) # https://www.geeksforgeeks.org/python-convert-string-to-binary/
        elif type(content) == np.ndarray:
            return [format(i, "08b") for i in content] # https://docs.replit.com/tutorials/python/steganography


    def hide_text(self, image, hiddenMessage):


        # times row,columns and three channels (r,g,b) to get full image size. Divided by 8 to get byte value
        totalPixels = image.shape[0] * image.shape[1] * 3 // 8
        print(f"You have a total of {totalPixels} bytes to encode")
        delimiter = "*****" # This will be important in the decode section
        binMessage = self.binary_converter(hiddenMessage + delimiter)
        numBits = len(binMessage)
        if numBits >= totalPixels:
            print("ERROR: Insufficient space, please reduce the size of the message")

        else:
            pass



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
