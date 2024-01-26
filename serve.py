from flask import Flask, request
import subprocess
import socket
import os

app = Flask(__name__)

def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Start a separate process to run stress_cpu.py
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'Stressing CPU in a separate process.'
    elif request.method == 'GET':
        # Return the private IP address of the EC2 instance
        return get_private_ip()

if __name__ == '__main__':
    # Make sure to set host to '0.0.0.0' to allow external requests
    app.run(host='0.0.0.0', port=5000)
