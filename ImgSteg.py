import cv2
import numpy as np


class ImgSteg:

    # Function to open and display image to user
    def open_image(self, image):
        image = cv2.imread(image, cv2.IMREAD_COLOR)
        cv2.imshow("Your Inputted image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return image

    # This function will be used to convert image pixels and the encoded message into their binary equivalent
    def binary_converter(self, content):
        if type(content) == str:
            return ''.join([format(ord(i), "08b") for i in content])
        elif type(content) == np.ndarray:
            return [format(i, "08b") for i in content]
        else:
            print("input not supported, please try again")


    # This function takes in code
    def encode_text(self, img, hiddenMessage):

        # Calculates size of the image
        maximumBytes = img.size
        print(maximumBytes)
        self.delimiter = "*****"
        # The below check ensures that the image has enough space to encode the user-supplied message
        if len(hiddenMessage+self.delimiter) > maximumBytes:
            print("\nERROR: Insufficient space, please increase the size of the image or reduce the message you are trying to encode.")
            quit()




if __name__ == "__main__":
    obj = ImgSteg()



