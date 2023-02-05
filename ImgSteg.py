import cv2
import numpy as np








class ImgSteg:

    print("\nWelcome to ImgSteg!!")

    # Function to open and display image to user
    def display_image(self, img):

        cv2.imshow("Your inputted image: ", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    # This function will be used to convert image pixels and the encoded message into their binary equivalent
    def binary_converter(self, content):
        if type(content) == str:
            return ''.join([format(ord(i), "08b") for i in content])

        elif type(content) == np.ndarray:
            return [format(i, "08b") for i in content]

        elif type(content) == np.uint8:
            return format(content, "08b")
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
        hiddenMessage += "*****"
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

    def encode_process(self):

        fileName = input("\nImage Filename with extension: ")
        if fileName.endswith("png"):
            image = cv2.imread(fileName)
            self.display_image(image)
            encodeMessage = input("Encoded Message: ")
            print("\nEncoding...")
            self.encodedImage = self.encoder(image, encodeMessage)
            self.dest = (fileName.removesuffix(".png") + "_encoded.png")
            cv2.imwrite(self.dest, self.encodedImage)
            print("\nyour image has been saved")

if __name__ == "__main__":
    obj = ImgSteg()
    obj.encode_process()


