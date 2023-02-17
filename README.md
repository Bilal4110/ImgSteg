# ImgSteg.py

---
### **Introduction**

**ImgSteg.py** is an opensource steganography tool which encodes and decodes messages within an image using the LSB (Least-significant bit)

The LSB method is ideal as it enables messages to be secretly hidden without changing the appearance of the image. For more information on this topic, please view the following resources:

- Steganography Explanation and Code Examples (Least Significant Bit) - https://www.youtube.com/watch?v=ZFGlJGwaN2w

- LSB Steganography Demo - https://www.youtube.com/watch?v=yNo58UiIMKU

- Image Steganography using Python - https://medium.com/towards-data-science/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372

### Required Modules

To ensures that this program runs properly, please ensure that the following modules are installed:

##### OpenCV

The OpenCV module is (expand) and can be installed using the following command:

```shell
pip install opencv-python
```
Numpy




### Instructions

1. To install the program either clone the repository (https://github.coventry.ac.uk/5062CEM/CW1-11207724.git) or download the ZIP file. 


2. To run the program, enter the following command into a terminal of your choice:

   ```Shell
   python3 ImgSteg.py
   ```

3. Once prompted, enter the path of your chosen image file. This will display your image. To exit this image display, press any key or select the exit button present at the top of the window. To ensure that images are efficiently encoded, please only supply .png images.

   ```
   Welcome to ImgSteg.py
   =============================================================
   
   Image Filename with extension (PNG files only): img.png
   ```


3. You will be then be prompted to enter a message. The message you provide will be encoded into the previously supplied image.

   ```
   Welcome to ImgSteg.py
   =============================================================
   
   Image Filename with extension (PNG files only): img.png
   
   Message to encode: This is a test...
   ```
   
4. Once the program is finished encoding, you will be asked if you wish to decode your previously encoded image. Please input "y" or "n" to confirm your choice.
   
   ```
   Welcome to ImgSteg.py
   =============================================================
   
   Image Filename with extension (PNG files only): img.png
   
   Message to encode: This is a test...
   
   Encoding...
   
   Your image has been encoded and saved as img_encoded.png
   
   =============================================================
   
   Do you wish to decode your image? (y/n):
   
   ```

5. If you choose to display 

### Algorithms Explanation

**Encoding**



**Decoding** - 


### Possible Improvements






