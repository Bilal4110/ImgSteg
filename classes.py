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



    def encode(self):
        height, width, channels = self.img.shape
        pixelArray = np.array(self.img)

        if channels == 3:
            n = 3
        elif channels == 4:
            n = 4

        totalPixels = pixelArray //self.n
        self.encodeMessage += "DDDDD" # Delimiter
        binaryMessage = ''.join([format(ord(i), "08b") for i in self.encodeMessage])
        requiredPixels = len(binaryMessage)

        if (requiredPixels > totalPixels).all():
            print("ERROR, please reduce your message or choose a bigger image ")
            quit()

        else:
            check_index=0
            for pixel in range(totalPixels):
                for q in range(0,3):
                    if check_index < requiredPixels:
                        pixelArray[pixel][q] = int(bin(pixelArray[p][q]) [2:9] + binaryMessage[pixel], 2)
                        check_index +=1
            pixelArray = pixelArray.reshape(height,width)
            cr



if __name__ == '__main__':
    obj = ImgSteg()
    obj.open_image()
    obj.encode()
