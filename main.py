import cv2  # An image proccessing library
import pytesseract  # an image to text library

# Configure the module
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r'C:\Users\natha\PycharmProjects\POE_prophecy\Capture3.PNG'
img = cv2.imread(path)
# Resize the image
new_dim = (int(img.shape[1] * 10), int(img.shape[0] * 10))
img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)
# Change contrast (alpha) and brightness (beta)
img = cv2.convertScaleAbs(img, alpha=2, beta=80)
cv2.imshow('img traiter1', img)
# Use OCR to read the text from the image
out_below = pytesseract.image_to_string(img)
# Print the text
print(out_below)
cv2.imshow('img traiter2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
