# Cryptogram using FaaS

This project is just a way for me to explore OpenFaaS. The main idea is to create an exercise where one should re-deploy the existing function with a new function with the correct translation map that decrypts the message. :)

A service on my RPi is using espeak TTS engine to speak out the returned messages. So there is a script that is scheduled to run regurarly that sends a hidden message to be translated.

Once the cryptogram has been resolved and pushed - the true meaning of the message will be revealed. 