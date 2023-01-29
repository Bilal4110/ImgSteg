import cv2


def open_image():  # This function is used to load the inputted image using the OpenCV module
    while True:
        fileName = input("\nImage Filename with extension: ")
        if fileName.endswith("png") or fileName.endswith("jpg") or fileName.endswith(
                "jpeg"):  # This checks to see if the image is valid
            opnImg = cv2.imread(fileName)
            cv2.imshow('Your inputted image: ', opnImg)
            cv2.waitKey(0)
            return opnImg

        else:
            print("\nPlease choose a valid image file!!")


def message_to_binary():  # Before encoding the image, we need to first convert the code to binary (https://www.thepythoncode.com/article/hide-secret-data-in-images-using-steganography-python)
    while True:
        encodeMessage = input("Encoded Message: ")
        # if type(encodeMessage) == str or type(encodeMessage) == int:
        if encodeMessage == "":
            print("\nPlease include a message to encode")
        else:
            enBin = ''.join([format(ord(i), "08b") for i in encodeMessage])
            print(f"\nYour message has been converted into binary: {enBin}")
            return enBin


def encode():
    opnImg = open_image()
    enBin = message_to_binary()



encode()
