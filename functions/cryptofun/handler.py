import string

def get_translation_dict():
    """ returns the translation dictionary
    """
    # The idea is to add the solution to the crypto here
    translation_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
                        'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
                        'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
                        'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
                        'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
                        'z': 'z'}
    return translation_dict

def decrypt_message(message):
    """decrypt a message
    Args:
       message (str) : encrypted message to be decrypted
    """
    translation_dict = get_translation_dict()
    message_lowercase = message.lower()

    translated_message = []
    for character in message_lowercase:
        # If a special character does not exist in the dict then use the original character
        encrypted_char = translation_dict.get(character, character)
        translated_message.append(encrypted_char)
    
    return ''.join(translated_message)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    return decrypt_message(req)