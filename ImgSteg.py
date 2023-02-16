import cv2  # OpenCV Module
import numpy as np  # Numpy Module


class Main:  # Creates a class called "Main"

    def __init__(self):
        self.dest = None  # This will be the location of the saved encoded image. This variable will also be used in the decoding process to decode the previously encoded image. Please note any string can be used as the delimiter as long as it is referenced in the decoding stage
        self.delimiter = "*****"  # This delimiter will be used in the decoding phase to prevent decoding issues

    def open_image(self, img):
        """
        This function opens and displays an image using the OpenCV module.

            :param img: This is the path of the image to be opened. This will be supplied by a user via the terminal.
            :type img: str
            :return image: Returns the data of the opened image in the form of a numpy array.
            :rtype image: numpy.ndarray
        """

        image = cv2.imread(img, cv2.IMREAD_ANYCOLOR)  # Loads an image from the supplied user input
        cv2.imshow("Your image", image)  # Shows the loaded image to the user with the heading "Your Image"
        cv2.waitKey(0)  # Keeps the image open until a user decides to press a key, or click on the exit button. https://pyimagesearch.com/2014/06/02/opencv-load-image/
        cv2.destroyAllWindows()  # Removes the opened window when an action is specified.
        return image  # Returns the image data in the form of a numpy array

    def data_to_binary(self, data):  # Creates a function to convert data types to binary
        """
        Converts a string (Binary message) or a numpy array (pixel) into its equivalent binary value

            :param data: Input data which needs to be converted into binary
            :type data: str or numpy.ndarray
            :return: The binary equivalent of the supplied data
            :rtype: string or list of strings in binary equivalent (Depending on the type of data inputted)
        """

        if type(data) == str:  # checks to see if the supplied data is a string (Message to be encoded)
            return ''.join(format(ord(i), '08b') for i in data)  # https://www.geeksforgeeks.org/python-convert-string-to-binary/
        elif type(data) == np.ndarray:  # this is the data in the opened image
            return [format(i, "08b") for i in data]  # https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372

    def binary_to_ascii(self, binaryData): #  Code taken from: https://www.javatpoint.com/image-steganography-using-python
        """
        This function converts binary values to their corresponding ASCII characters.

            :param binaryData: Binary data that needs to be converted into ASCII characters
            :type binaryData: str
            :return: Returns the ASCII character from the binary values that were inputted
            :rtype: str
        """

        allBytes = [binaryData[i: i + 8] for i in range(0, len(binaryData), 8)]
        decodedData = ""
        for bytes in allBytes:
            decodedData += chr(int(bytes, 2))
        return decodedData  # Returns the decoded string, so it can be displayed to the user

    def hide_text(self, image, hiddenMessage):
        """
        This function hides a text-based message into an image using the LSB method. It first calculates the sizes of both the image and the message (with delimiter) which needs to be encoded.
        This is to ensure that there enough available bytes to encode. If there is enough space, then a message is encoded within the least significant bits of the image's pixels.

            :param image: Image which will be used to store the encoded message (Cover Image)
            :param hiddenMessage: Message that will be encoded and hidden into the image. This is to be supplied by the user in the form of an input
            :type image: numpy.ndarray
            :type hiddenMessage: str
            :returns: The modified image data containing the hidden message encoded within its pixels
            :rtype: numpy.ndarray
            """

        totalBytes = image.size // 8  # calculates the total size of the image
        if len(hiddenMessage + self.delimiter) >= totalBytes:
            print("ERROR: Insufficient space, please reduce the size of the message")
            quit()
        else:
            binaryMessage = self.data_to_binary(hiddenMessage + self.delimiter)  # Binary equivalent of the both the delimiter and the message to be encoded
            binaryLength = len(binaryMessage)
            checkIndex = 0 # ADD COMMENT - https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
            for row in image: # ADD COMMENT -  https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                for pixel in row: # ADD COMMENT - https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                    r, g, b = self.data_to_binary(pixel) # ADD COMMENT - https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                    for x in range(3):
                        if checkIndex < binaryLength:
                            channel = [r, g, b][x]
                            modifiedLSB = int(channel[:-1] + "0")
                            pixel[x] = modifiedLSB + int(binaryMessage[checkIndex])
                            checkIndex += 1
                    if checkIndex >= binaryLength:
                        break
                return image

    def show_text(self, encodedImage):
        """
        This function displa


        :param encodedImage:
        :return:
        """
        binaryMessage = ""
        for row in encodedImage:
            for pixels in row:
                r, g, b = self.data_to_binary(pixels) # splits pixels into r,g,b and then converts them to their binary equivalent -
                for x in range(3): # loops 0 - 2 (0 = Red, 1 = Green, and 2 = Blue)
                    channel = [r, g, b][x] # Selects one of the r,g,b color channels
                    binaryMessage += str(channel[-1])# Adds the LSB value of each channel (r,g,b) into the BinaryMessage variable
                    if self.delimiter in self.binary_to_ascii(binaryMessage): # This checks to see if the delimiter is found within the binary message. If so, the previous for loop will stop. https://stackoverflow.com/questions/9797446/how-to-remove-certain-characters-from-a-variable-python
                        text = self.binary_to_ascii(binaryMessage) # This converts the extracted binary values (with the delimiter)
                        message = text.replace(self.delimiter, "") # https://stackoverflow.com/questions/9797446/how-to-remove-certain-characters-from-a-variable-python
                        return message

    def encode(self):
        fileName = input("\nImage Filename with extension (PNG files only): ")
        if fileName.endswith("png"):
            img = self.open_image(fileName)

            encodeMessage = input("Message to encode: ")
            if len(encodeMessage) == 0:
                print("\nERROR: Please add a message to encode!")
                quit()

            print("\nEncoding...")
            encodedImage = self.hide_text(img, encodeMessage)
            self.dest = (fileName.removesuffix(".png") + "_encoded.png")
            cv2.imwrite(self.dest, encodedImage)
            print("\nYour image has been saved...")

        else:
            print("\nERROR: Please supply a png image")
            exit()

    def decode(self):
        choice = input("\nDo you wish to decode your image? (y/n): ")
        if choice == "y" or choice == "Yes" or choice == "Y":
            encodedImg = cv2.imread(self.dest)
            print(f"\nDecoded Message: {self.show_text(encodedImg)}")

        elif choice == "n" or choice == "no":
            print("\nQuiting...")
            quit()

        else:
            print("\nERROR: Please choose a valid option (y/n)")


if __name__ == "__main__":
    obj = Main()
    obj.encode()
    obj.decode()
