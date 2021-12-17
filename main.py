import argparse
import winsound
from tkinter import *

import cv2  # An image proccessing library
import keyboard
import pyautogui  # library to take screenshot
import pytesseract  # library to transform an image to text library


# from prophecy_overview import prophecy_overview

def submit_click(prophecy_name, dictionary):
    try:
        int(price.get())
        dictionary[prophecy_name] = int(price.get())
        with open('prophecy_overview.csv', 'w') as file:
            for i in dictionary.keys():
                file.write("%s; %s\n" % (i, dictionary[i]))
        window.destroy()
    except ValueError:
        message.configure(text='Error, try again')


if __name__ == '__main__':
    comm = argparse.ArgumentParser(description="Check and save the value of prophecy")
    comm.add_argument('--min', type=int, help="minimum value you want to keep")
    args = comm.parse_args()

    min_price = args.min or 10
    prophecy_overview = dict()
    with open("prophecy_overview.csv") as file:
        for line in file:
            line = line.strip('\n')
            (key, val) = line.split(";")
            prophecy_overview[key] = int(val)
    # Configure the module tesseract
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

            # Use OCR to read the text from the image and clean the result in a string

            out_below = pytesseract.image_to_string(img)
            x = out_below.split()
            final = ""
            for i in x:
                final += i + " "
            final = final[:-1]

            # return the result with a sound signal

            if final in prophecy_overview and prophecy_overview[final] >= min_price:
                winsound.Beep(860, 100)
            elif final in prophecy_overview and prophecy_overview[final] < min_price:
                winsound.Beep(350, 100)
            else:
                window = Tk()
                window.title('recording')
                libelle = Label(window, text=final + ' prophecy_name is not yet registered. Please price it.')
                libelle.pack()
                price = Entry(window)
                price.focus_set()
                price.pack(pady=10)
                message = Label(window, text='')
                message.pack(padx=10, pady=(0, 10))
                button_submit = Button(window, text='Submit', command=lambda: submit_click(final, prophecy_overview))
                button_submit.pack(padx=10, pady=(0, 10))
                button_finish = Button(window, text='Do not register', command=window.destroy)
                button_finish.pack(padx=10, pady=(0, 10))
                window.mainloop()
