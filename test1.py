import cv2
import numpy as np



def message_to_binary():  # Before encoding the image, we need to first convert the code to binary (https://www.thepythoncode.com/article/hide-secret-data-in-images-using-steganography-python)
    while True:
        encodeMessage = input("Encoded Message: ")
        print(type(encodeMessage))
        if encodeMessage == "":
            print("\nPlease include a message")

        else:
            enBin = ''.join([format(ord(i), "08b") for i in encodeMessage])
            print(f"\nYour message has been converted into binary: {enBin}")
            break

# type(encodeMessage) == str:


def encode_image():
    while True:
        fileName = input("\nImage Filename with extension: ")
        if fileName.endswith("png") or fileName.endswith("jpg") or fileName.endswith("jpeg"):  # This checks to see if the image is valid
            opnImg = cv2.imread(fileName)
            cv2.imshow('Your inputted image: ', opnImg)
            cv2.waitKey(0)
            noBytes =  opnImg.shape[0] * opnImg.shape[1] * 3 // 8
            print("[*] Maximum bytes to encode:", noBytes)
            break
        else:
            print("\nPlease choose a valid image file!!")


encode_image()
message_to_binary()

