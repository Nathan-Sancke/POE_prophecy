# Import some modules
import cv2 # An image proccessing library
import pytesseract # an image to text library
import numpy as np # used for mathematics but can be used in image proccessing

# Configure the module
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = r'C:\Users\natha\PycharmProjects\POE_prophecy\Capture3.PNG'
# Make the image grey
img_4x = cv2.imread(image)
gray = cv2.cvtColor(img_4x, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)
kernel = np.ones((2, 1), np.uint8)
img_4x = cv2.erode(gray, kernel, iterations=1)
img_4x = cv2.dilate(img_4x, kernel, iterations=1)
# Use OCR to read the text from the image
out_below = pytesseract.image_to_string(img_4x)
# Print the text
print(out_below)

