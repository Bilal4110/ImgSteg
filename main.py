import cv2

filename = input("Image Filename with extension: ")
encoded = input("Encoded Message: ")

print(f"\nImage = {filename} \nSecret message = {encoded}")


if filename.endswith("png"):
    print("correct")

else:
    print("\nPlease add an image with png suffix")

