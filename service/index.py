from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route("/api/message", methods=['POST'])
def send_message():
    message = request.json['message']
    os.system('espeak \"%s\" --stdout |aplay' % message)
    return "Speaking"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)