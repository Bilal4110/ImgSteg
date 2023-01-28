import cv2


# print(f"\nImage = {fileName}")


def open_image():  # This function is used to load an image
    while True:
        fileName = input("\nImage Filename with extension: ")
        if fileName.endswith("png") or fileName.endswith("jpg") or fileName.endswith("jpeg"):
            opnImg = cv2.imread(fileName)
            cv2.imshow('Your inputted image: ', opnImg)
            cv2.waitKey(0)
            break

        else:
            print("\nPlease include a valid image!!")


open_image()


def encoding():
    encode = input("Encoded Message: ")
    return ("test")


encoding()
