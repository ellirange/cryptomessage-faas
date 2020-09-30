FROM python:3-alpine
WORKDIR /app
RUN apk update
RUN apk add musl-dev gcc espeak alsa-utils
RUN pip3 install --upgrade pip
RUN pip3 install flask
COPY . .
ENV PYTHONPATH "${PYTONPATH}:/app"
CMD ["python3", "index.py"]