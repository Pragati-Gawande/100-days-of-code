import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"E:\Terrssrect\tesseract.exe"

def convert():
    img = Image.open('test3.jpeg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()    
