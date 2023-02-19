# ImgSteg.py

-----

## Introduction

**ImgSteg.py** is an open-source steganography tool which encodes and decodes messages within an image using the least significant bit (LSB) method. The LSB method is a very effective approach to encoding, as it enables messages to be secretly hidden without changing the appearance of the image. For more information related to this topic, please view the following links:

- Steganography Explanation and Code Examples (Least Significant Bit) - https://www.youtube.com/watch?v=ZFGlJGwaN2w

- LSB Steganography Demo - https://www.youtube.com/watch?v=yNo58UiIMKU

- Image Steganography using Python - https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372

## Required Modules

To ensure that this program runs correctly, please ensure that the following modules are installed:

#### OpenCV

OpenCV is an open-source library which is widely used for computer vision, machine learning and image processing. It can be installed onto your system using the following command:

```shell
pip install opencv-python
```


#### NumPy

NumPy is an open-source Python library which is used for mathematical calculations. OpenCV represents images as a NumPy array, which consists of values that represent pixels. NumPy usually comes preinstalled with OpenCV. However, If it does not, it can be installed with the following command:

```shell
pip install numpy
```

For a full guide on installing all the necessary libraries for this program, please view the following link: https://github.coventry.ac.uk/pages/CUEH/5062CEM/labs/tutorials/OpenCV_WSL/


## Instructions

1. To install the program either clone the repository (https://github.coventry.ac.uk/5062CEM/CW1-11207724.git) or download the ZIP file present on GitHub. 


2. To run the program, enter the following command into a terminal of your choice:

   ```Shell
   python3 ImgSteg.py
   ```


3. Once you run the program, you will be shown a menu. Please choose a valid option: 1 to encode an image, 2 to decode a previously encoded image, or 3 to exit the program. 

   ```
   Welcome to ImgSteg.py
   ======================
   
   1. Encode an Image.
   
   2. Decode an Image.
   
   3. Exit the program.
   
   Select Option:
   ```

### Encoding an Image
   
1. After inputting 1 into the terminal, you will be prompted to provide an image and message to encode. If the image you wish to encode is not located in the same directory as the program, please provide the full path of the image when prompted.  

   ```
   Select Option: 1
   ===========================
   
   Image Filename with Extension (PNG files only): img.png
   
   Message to encode: This is a test
   ```

2. After supplying the required information and pressing enter. The message will then be encoded into the previously supplied image. Once this process has taken place, the newly encoded image will be saved with the suffix _encoding.png (as seen below). The program will then quit, enabling the image to properly save. 

   ```
   Select Option: 1
   ===========================
   
   Image Filename with Extension (PNG files only): img.png
   
   Message to encode: This is a test
   
   Image has been encoded successfully.
   
   Image has been saved as img_encoded.png.
   =================================================================
   ```

### Decoding an Image

1. To decode a previously encoded image, input 2 when prompted.

   ```
   Welcome to ImgSteg.py
   ======================

   1. Encode an Image.

   2. Decode an Image.

   3. Exit the program.

   Select Option: 2
   ```

2. You will then be asked to input the name of an image file to decode. If the image you wish to decode is not located in the same directory as the program,please provide the full path of the image when prompted.

   ```
   Select Option: 2
   =========================
   
   Image to decode: img_encoded.png
   ```
   
3. Once you have provided an image to decode, the decoded message will be displayed in the terminal. 
   
   ```
   Select Option: 2
   =========================
   
   Image to decode: img_encoded.png
   
   Your decoded message is: This is a test
   =================================================================
   ```

### Exiting the Program

1. To exit the program, enter 3 when prompted by the interactive menu.

   ```
   Welcome to ImgSteg.py
   ======================
   
   1. Encode an Image.
               
   2. Decode an Image.
               
   3. Exit the program.
               
   Select Option: 3
   ```

2. The program will now exit.

   ```
   Select Option: 3
   ======================
   
   Exiting....
   =================================================================
   ```











