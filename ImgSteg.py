import cv2  # Imports OpenCV Module as cv2.
import numpy as np  # Imports numpy module as np.


class Main:  # Creates a class called "Main"

    def __init__(self):
        """
        This function creates a new instance of the Main class.

            :Attribute dest: The file path of the saved encoded image
            :Attribute delimiter: This string is used to separate the encoding message from the image data during the decoding process.
            :type self.dest: str
            :type self.delimiter: str
        """
        self.delimiter = "*****"  # This delimiter will be used in the decoding phase to prevent possible decoding issues. Please note any string can be used as the delimiter as long as it is referenced in the decoding stage.

    def open_image(self, img):
        """
        This function opens and displays an image using the OpenCV module.

            :param img: This is the path of the image to be opened. This will be supplied by a user via the terminal.
            :type img: str
            :return image: Returns the data of the opened image.
            :rtype image: numpy.ndarray
        """

        image = cv2.imread(img, cv2.IMREAD_ANYCOLOR)  # Reads and loads an image from the supplied user input. The provided image can be read in any color
        cv2.imshow("Your image", image)  # Displays the loaded image to the user with the heading "Your Image".
        cv2.waitKey(0)  # Keeps the image open indefinitely until a user decides to press a key, or click on the exit button. https://pyimagesearch.com/2014/06/02/opencv-load-image/
        cv2.destroyAllWindows()  # Removes the opened window when an action is specified.
        return image  # Returns the image data in the form of a numpy array.

    def data_to_binary(self, data):  # Creates a function to convert data types to binary
        """
        Converts a string (Binary message) or a numpy array (pixel) into its equivalent binary value.

            :param data: Input data which needs to be converted into binary
            :type data: str or numpy.ndarray
            :return: The binary equivalent of the supplied data
            :rtype: string or list of strings in binary equivalent (Depending on the type of data inputted)
        """

        if type(data) == str:  # Checks to see if the supplied data is a string. This is the message which is to be encoded into the user supplied image.
            return ''.join(format(ord(i), '08b') for i in data) # Converts a string of ASCII characters into binary values. Code taken from: https://www.geeksforgeeks.org/python-convert-string-to-binary/
        elif type(data) == np.ndarray:  # Checks to see if the supplied data is an numpy.ndarray. This is the data present within the image to be encoded.
            return [format(i, "08b") for i in data] # Converts array of RGB pixels (ndarray) into their binary equivalents. Code taken from: https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372


    def binary_to_ascii(self, binaryData): # Code in this function has been taken from: https://www.javatpoint.com/image-steganography-using-python
        """
        This function converts binary values to their corresponding ASCII characters.

            :param binaryData: Binary data that needs to be converted into ASCII characters
            :type binaryData: str
            :return: Returns the ASCII character from the binary values that were inputted
            :rtype: str
        """

        allBytes = [binaryData[i: i + 8] for i in range(0, len(binaryData), 8)]
        decodedData = "" # Creates an empty string under the variable "decodedData". This will be used to store the converted message.
        for bytes in allBytes:
            decodedData += chr(int(bytes, 2))
        return decodedData  # Returns the decoded string, so it can be displayed to the user

    def hide_text(self, image, hiddenMessage):
        """
        This function hides a text-based message into an image using the LSB method.
        It first calculates the sizes of both the image and the message (with delimiter) which needs to be encoded.
        This is to ensure that there enough available bytes to encode. If there is enough space, then the user supplied message is encoded within the least significant bits of the image's pixels.

            :param image: Image which will be used to store the encoded message (Cover Image)
            :param hiddenMessage: Message that will be encoded and hidden into the image. This is to be supplied by the user in the form of an input
            :type image: numpy.ndarray
            :type hiddenMessage: str
            :returns: The modified image data containing the hidden message encoded within its pixels
            :rtype: numpy.ndarray
            """

        totalBytes = image.size # calculates the total size of the image.
        binaryMessage = self.data_to_binary(hiddenMessage + self.delimiter)  # Binary conversion of the both the delimiter and the message to be encoded. This is done by using the previously created data_to_binary function
        binaryLength = len(binaryMessage) # Calculates the length of the "binaryMessage" variable and stores it under the "binaryLength" variable.
        if binaryLength >= totalBytes: # Checks to see if the size of the binary message is greater or equal to the size of the message. This is to ensure that there is adequate space for encoding the message.
            print("ERROR: Insufficient space. Please reduce the size of the message or select a bigger image.") # Prints a warning error message to the user informing them that the message is too big to encode within the image. Suggestion are also made to solve this issue.
            quit() # Quits the program.
        else: # If the length of the message is less than the image size:
            Index = 0 # Creates an index which will be used to track the position of the binary message. This concept has been taken from: https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
            for row in image: # This loop goes over each row present within the image. Essentially this a line of pixels. Loop taken from:  https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                for pixel in row: # This loop iterates over each pixel present in that specific row.  Loop taken from: https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                    r, g, b = self.data_to_binary(pixel) # splits pixels into r,g,b and then converts them to their binary equivalent. Concept taken from:  https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                    for x in range(3): # loops 0 - 2 (0 = Red, 1 = Green, and 2 = Blue).
                        if Index < binaryLength: # Checks to see if the index is less than the length of the binary message.
                            channel = [r, g, b][x] # Selects one of the r,g,b color channels depending on the value of x.
                            modifiedLSB = int(channel[:-1] + "0") # Changes the LSB (1st bit to the right) of the r, g or b pixels to 0. This is in preparation to allow the binary message to be encoded within the LSBs.
                            pixel[x] = modifiedLSB + int(binaryMessage[Index])  # Adds each binary value from the message into the LSBs depending on the position of x and the index.
                            Index += 1 # Adds 1 to the Index variable.
                    if Index >= binaryLength: # Checks to see if the Index is greater than, or equal to the length of the binary message
                        break # Stops the loop.
                return image # Returns the modified image data with the encoded message and delimiter embedded within the LSBs of the image.


    def encode(self):
        """
        Encodes a message into a PNG image file. The user is asked to input a .png image file as well as a message to encode. The hide_text function will be called to embed the message into the image.
        Due to lossy compression algorithms present within .jpeg files, only png files are accepted in this program. More information regarding this can be found at: https://odsc.medium.com/study-finds-novel-method-of-resolving-jpeg-compression-defects-in-computer-vision-datasets-78a325fbeda0.
        Once the encoding has finished, the image is saved with the appended suffix "_encoded.png".
        """
        print("===========================")
        fileName = input("\nImage Filename with Extension (PNG files only): ") # Ask the user to input an image file name. Due to compression concerns only PNG files will be accepted by this program.
        if fileName.endswith("png"): # Checks to verify that  the filename adds with the .png suffix.
            img = self.open_image(fileName) # Opens the inputted image filename using the previously created open_image function.

            encodeMessage = input("\nMessage to encode: ") # Ask the user to input a message to encode into the previously supplied image.
            if len(encodeMessage) == 0: # Checks to see if the encodedMessage variable is empty.
                print("\nERROR: Please add a message to encode!") # Error message instructing the user to supply a message to encode.
                quit() # Quits the program

            print("\nEncoding...") # Print statement to inform users that the encoding process is taking place.
            encodedImage = self.hide_text(img, encodeMessage) # Takes the previous user inputs (image and message to encode) and passes them to the hide_text function.
            dest = (fileName.removesuffix(".png") + "_encoded.png") # Removes the suffix ".png" from the encoded image, and adds the new "_encoded.png" to the end of the filename.
            cv2.imwrite(dest, encodedImage) # Saves the encoded image under the predefined filename.
            print(f"\nYour image has been encoded and saved as {dest}")  # Print statement to inform users that the image has been encoded and saved.
            print("=================================================================")

        else:
            print("\nERROR: Please supply a png image") # Error statement if a non .png image is inputted by the user.
            quit() # Quits the program

    def decode(self):
        """

        Extracts a hidden text from an encoded Image's pixels using the LSB method.
        Once the text is extracted, the delimiter is removed from the text to form a message which can be returned to the user.

            :param encodedImage: A numpy array which represents the previously encoded image.
            :type encodedImage: numpy.ndarray
            :return: The hidden encoded text message which was taken from the image.
            :rtype: str
        """
        print("=========================")
        imageName = input("\nImage to decode: ") # Asks the user to supply an image to decode.
        encodedImage = self.open_image(imageName) # Opens the previously supplied image using the previously created open_image() function.
        binaryMessage = "" # Creates an empty string under the "binaryMessage" variable. This will be used to store the extracted binary message.
        for row in encodedImage: # This loop goes over each row present within the encoded image. Essentially this a line of pixels. Loop taken from:  https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
            for pixels in row: # This loop iterates over each pixel present in that specific row. Loop taken from: https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
                r, g, b = self.data_to_binary(pixels) # splits pixels into r,g,b and then converts them to their binary equivalent.
                for x in range(3): # loops 0 - 2 (0 = Red, 1 = Green, and 2 = Blue).
                    channel = [r, g, b][x] # Selects one of the r,g,b color channels.
                    binaryMessage += (channel[-1])# Adds the LSB value of each channel (r,g,b) into the BinaryMessage variable.
                    if self.delimiter in self.binary_to_ascii(binaryMessage): # This checks to see if the delimiter is found within the binary message. If so, the previous for loop will stop. Concept taken from: https://stackoverflow.com/questions/9797446/how-to-remove-certain-characters-from-a-variable-python
                        text = self.binary_to_ascii(binaryMessage) # This converts the extracted binary values (with the delimiter) into ASCII characters.
                        message = text.replace(self.delimiter, "") # Removes the delimiter from the string by replacing it with an empty string value (""). Concept taken from: https://stackoverflow.com/questions/9797446/how-to-remove-certain-characters-from-a-variable-python
                        return message # Returns the decoded message to the user.


    def menu(self):
        """
        This function creates a menu that allows an end user to select an option to either encode, decode or exit the program.
        A while loop has been implemented to ensure that the user selects a valid option.
        """
        while True:
            print("\nWelcome to ImgSteg.py") # Welcome message
            print("======================")
            choice = input("""\n1. Encode an Image.
            \n2. Decode an Image.
            \n3. Exit the program.
            \nSelect Option: """) # This input field creates the interface for the menu.

            if choice == "1": # If the user inputs "1" into the terminal...
                self.encode() # Calls the encoding functions to embed a message into an image
                break # Breaks the loop so that the encoded image can be saved.

            if choice == "2":
                decodedMessage = self.decode() # Assigns a variable to the decode function so that the output can be printed to the user
                print(f"\nYour decoded message is: {decodedMessage}") # Prints the decoded message to the user.
                break # Breaks the loop once the decoded message is displayed

            if choice == "3": # If the user inputs "3" into the terminal...
                print("\nExiting....") # Informs the end user that the program is quitting
                exit() # Exits the program








if __name__ == "__main__": # Ensures that the program is only executed if it is being directly being run as a main program, and not when imported as a module in another python script.
    obj = Main() # Creates instance of the "main" class and stores it in the "obj" variable.
    obj.menu() # Calls the menu function from the "main" class to display the menu.


"""Possible Implementations

To further improve the functionality of this program, the following suggestions have been provided:

1. Utilise an encryption key to safely encode and decode a message into an image.
2. A password could be added to ensure that only authorised users can decode the message within the image.
3. Create more functions to embed a wide variety of digital data such as images and audio files into other images. 

"""

#INT CHECK
