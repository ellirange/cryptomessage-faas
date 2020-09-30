import string
import random
import sys

def create_crypto():
    """create cryptomap
    """
    alphabet = list(string.ascii_lowercase)
    alphabet_copy = alphabet.copy()
    random.shuffle(alphabet_copy)
    encoding_dict = {x : y for x,y in zip(alphabet, alphabet_copy)}
    return encoding_dict

def translate_message(translation_dict, message):
    """translate message using the translation dict
    Args:
        translation_dict (dict): a dictionary with char -> char to translate message to encrypted
        message (string): message to be translated
    """
    translated_message = []
    for character in message:
        # If a special character does not exist in the dict then use the original character
        encrypted_char = translation_dict.get(character, character)
        translated_message.append(encrypted_char)
    
    return ''.join(translated_message)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    crypto = create_crypto()
    message = translate_message(crypto, req)
    return {"crypto map" : crypto,
            "message" : message}
    

