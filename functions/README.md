# FaaS functions

**Note - this project is for creating and solving a cryptogram, which is a puzzle. So just for fun, nothing else.** https://en.wikipedia.org/wiki/Cryptogram

create-cryptogram (create_crypto.yml) - this function takes an input message to be decrypted and returns the "encoding map" and encoded message

crypto-function (cryptofun.yml) - takes a message as an input and returns a translated message. Once the cryptogram has been resolved the true message will be revealed.

To deploy these functions run
```console
user@machine:~$ faas-cli up -f create_crypto.yml
```
```console
user@machine:~$ faas-cli up -f cryptofun.yml
```