import cv2
import numpy as np








class ImgSteg:

    # This function will be used to convert image pixels and the encoded message into their binary equivalent
    def binary_converter(self, content):


        if type(content) == str:
            return ''.join([format(ord(i), "08b") for i in content])

        elif type(content) == int or type(content) == np.uint8:
            return format(content, "08b")

        elif type(content) == bytes or type(content) == np.ndarray:
            return [format(i, "08b") for i in content]

        else:
            print("input not supported, please try again")

    # This function takes in code
    def encoder(self, img, hiddenMessage):

        # Calculates size of the image
        maximumBytes = img.size // 8

        # The below check ensures that the image has enough space to encode the user-supplied message
        if len(hiddenMessage) > maximumBytes:
            print("\nERROR: Insufficient space, please increase the size of the image or reduce the message you are trying to encode!!!")

        # This is the delimiter which will be added to the message. (Any string can be used as a delimiter)
        hiddenMessage += "====="
        binaryMessage = self.binary_converter(hiddenMessage)
        dataLength = len(binaryMessage)
        index = 0
        for values in img:
            for pixel in values:
                # splits pixels into r,g,b and then converts them to their binary equivalent (ADD REFERENCE)
                r, g, b = self.binary_converter(pixel)
                if index < dataLength:
                    pixel[0] = int(r[:-1] + binaryMessage[index], 2)
                    index += 1
                if index < dataLength:
                    pixel[1] = int(g[:-1] + binaryMessage[index], 2)
                    index += 1
                if index < dataLength:
                    pixel[2] = int(b[:-1] + binaryMessage[index], 2)
                    index += 1

                if index >= dataLength:
                    break

        return img





if __name__ == "__main__":
    obj = ImgSteg()


