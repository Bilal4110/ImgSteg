import cv2
import numpy as np


class ImgSteg:
    fileName = input("\nImage Filename with extension (Please choose PNG images to ensure efficiency): ")
    img = cv2.imread(fileName)
    encodeMessage = input("Encoded Message:")

    def open_image(self):
        if self.fileName.endswith("png") or self.fileName.endswith("jpg") or self.fileName.endswith(
                "jpeg"):  # Check to see if inputted filename is a valid image.
            cv2.imshow('Your inputted image: ', self.img)
            cv2.waitKey(0)
        elif self.fileName == "":
            print("\nERROR: Can not leave filename empty. Please try again")
            quit()
        else:
            print("\nERROR: Please choose a valid image.")
            quit()

    def message_check(self):
        if self.encodeMessage == "":
            print("ERROR: Please include a message to encode")
            quit()

    def encode(self):
        height, width = self.img.shape[0], self.img.shape[1]
        pixelArray = self.img.ravel()
        print(pixelArray)
        totalPixels = pixelArray.size // 3
        self.encodeMessage += "DDDDD"  # Delimiter
        binaryMessage = ''.join([format(ord(i), "08b") for i in self.encodeMessage])
        requiredPixels = len(binaryMessage)

        if requiredPixels > (totalPixels * 3):
            print("ERROR, please reduce your message or choose a bigger image ")
            quit()

        else:
            check_index = 0
            for p in range(totalPixels):
                for q in range(0, 3):
                    if check_index < requiredPixels:
                        pixelArray[p][q] = int(bin(pixelArray[p][q])[2:9] + binaryMessage[check_index], 2)
                        check_index += 1

            array = pixelArray.reshape(height, width, 3)
            encodedImage = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
            dest = input("Where do you wish to store the image")
            cv2.imwrite(dest, encodedImage)
            # encodedImage = cv2.cvtColour (array, cv2.COLOR_RGB2BGR)
            # cv2.imwrite(f"{self.fileName}+_encoded.png", encodedImage)
            print("Your message has been successfully encoded")


if __name__ == '__main__':
    obj = ImgSteg()
    obj.open_image()
    obj.message_check()
    obj.encode()
