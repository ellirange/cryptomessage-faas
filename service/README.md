# The "speaking" service

I did a fast and simple small service that uses espeak for text-to-speech on one of my RPis. I did not get it to work with the python package, until then I am using os.system.

I got it to work on my RPi by running this.

```console
user@machine:~$ docker run -i -t -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/snd -p 80:80  <image-name>
```