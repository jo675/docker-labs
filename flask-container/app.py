from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world from Python Flask\n' + 'Greetings from container: ' + socket.gethostname()

app.run(host='0.0.0.0', port=81)