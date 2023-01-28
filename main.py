import cv2

filename = input("Image Filename with extension: ")
encoded = input("Encoded Message: ")

print(f"\nImage = {filename} \nSecret message = {encoded}")


def open_image(filename):
    if filename.endswith("png"):
        opnImg = cv2.imread(filename)
        cv2.imshow('Your image: ', opnImg)
        cv2.waitKey(0)

    else:
        print("\nPlease add an image with the png suffix")


open_image(filename)

#cv2.imwrite('dog.jpg', opnImg)