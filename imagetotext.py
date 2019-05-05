# -*- coding: utf-8 -*-
"""
Created on Sun May  5 12:11:02 2019

@author: Monish
"""

import pytesseract as pyt #pip install pytesseract 
from PIL import Image as i


l = i.open('test 3.jpg') 
pyt.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Use the Location of your Tesseract 
output =pyt.image_to_string(l)

with open('magic3.txt', mode ='w') as file:
 file.write(output)
