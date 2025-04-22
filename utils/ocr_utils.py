# import pytesseract
# from gtts import gTTS
# import os

# # Ensure Tesseract is configured correctly
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path if needed

# def extract_text(image):
#     """
#     Extracts text from a preprocessed image using Tesseract OCR.
#     """
#     try:
#         text = pytesseract.image_to_string(image, lang='eng')  # 'eng' for English
#         return text
#     except Exception as e:
#         print(f"Error during text extraction: {e}")
#         return ""

# def text_to_speech(text):
#     """
#     Converts the extracted text to speech and saves it as an audio file.
#     """
#     try:
#         if text.strip():  # Ensure there's text to convert
#             tts = gTTS(text=text, lang='en')
#             audio_path = 'static/output_audio.mp3'
#             tts.save(audio_path)
#             return audio_path
#         else:
#             return None
#     except Exception as e:
#         print(f"Error during text-to-speech conversion: {e}")
#         return None



import pytesseract
from gtts import gTTS
import os
import logging

# Ensure Tesseract is configured correctly (path might need adjusting for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if needed

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def extract_text(image):
    """
    Extracts text from a preprocessed image using Tesseract OCR.
    """
    try:
        text = pytesseract.image_to_string(image, lang='eng')  # Use 'eng' for English
        logging.debug(f"Extracted Text: {text}")
        return text
    except Exception as e:
        logging.error(f"Error during text extraction: {e}")
        return ""

def text_to_speech(text):
    """
    Converts extracted text to speech and saves it as an audio file.
    """
    try:
        if text.strip():  # Ensure there is text to convert
            tts = gTTS(text=text, lang='en')
            audio_path = 'static/output_audio.mp3'  # Save audio in the static folder
            tts.save(audio_path)
            logging.debug(f"Audio saved at: {audio_path}")
            return audio_path
        else:
            logging.warning("No text to convert to speech.")
            return None
    except Exception as e:
        logging.error(f"Error during text-to-speech conversion: {e}")
        return None
