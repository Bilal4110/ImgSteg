import cv2
import numpy as np


class MyClass:
    fileName = input("\nImage Filename with extension (Please choose PNG images to ensure efficiency): ")
    img = cv2.imread(fileName)
    encodeMessage = input("Encoded Message:")
    n = 0

    def open_image(self):
        if self.fileName.endswith("png") or self.fileName.endswith("jpg") or self.fileName.endswith(
                "jpeg"):  # Check to see if inputted filename is a valid image.
            cv2.imshow('Your inputted image: ', self.img)
            cv2.waitKey(0)
        elif self.fileName == "":
            print("\n ERROR: Can not leave filename empty")
            quit()
        else:
            print("\nERROR: Please choose a valid image")
            quit()

    def encode(self):
        pixel_array = np.array(self.img)

        height, width, channels = self.img.shape
        if channels == 3:
            print("image is RGB")
            self.n = 3
        elif channels == 4:
            print("image is RGBA")
            self.n = 4
        total_pixels = pixel_array // self.n
        self.encodeMessage += "#####" # Delimiter
        binaryMessage = ''.join([format(ord(i), "08b") for i in self.encodeMessage])
        print(binaryMessage)
        requiredPixels = len(binaryMessage)

        if (requiredPixels > total_pixels).all():
            print("ERROR, please reduce your message or choose a bigger image ")
            quit()




if __name__ == '__main__':
    obj = MyClass()
    obj.open_image()
    obj.encode()
