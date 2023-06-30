# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:45:47 2023

@author: PC
"""

import pdfplumber as pp
from gtts import gTTS
#Extract text from pdf
pdf_text = ''

with pp.open('attention_is_all_you_need.pdf') as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text()
#Convert extracted text to speech
tts = gTTS(text=pdf_text, lang='en')
tts.save('audio_book.mp3')