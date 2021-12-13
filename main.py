import cv2  # An image proccessing library
import pytesseract  # an image to text library
import pyautogui  # library to take screenshot
import keyboard

# Configure the module
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r'C:\Users\natha\PycharmProjects\POE_prophecy\screenshot.PNG'
while True:
    if keyboard.is_pressed('ctrl+alt+f'):  # activates the script when you do ctrl+alt+d
        img = pyautogui.screenshot(region=(250, 320, 170, 34))  # take a screenshot
        img.save(path)
        img = cv2.imread(path)
        # Resize the image
        new_dim = (int(img.shape[1] * 10), int(img.shape[0] * 10))
        img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)
        # Change contrast (alpha) and brightness (beta)
        img = cv2.convertScaleAbs(img, alpha=1.4, beta=80)
        cv2.imshow('img traiter1', img)
        # Use OCR to read the text from the image
        out_below = pytesseract.image_to_string(img)
        # Print the text
        print(out_below)
