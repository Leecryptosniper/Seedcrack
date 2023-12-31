# app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO
import subprocess
import threading
import os
import json

# Import the generate_header function from header.py
from header import generate_header

app = Flask(__name__)
socketio = SocketIO(app)

def run_scripts():
    # Code to execute the run_scripts.bat script
    subprocess.run(['run_scripts.bat'])

    # Notify the client that the script has completed
    socketio.emit('script_completed', {'status': 'success'})

    # Broadcast an event to inform the client about new wallets
    socketio.emit('wallets_updated')

@app.route('/')
def index():
    # Use the generate_header function to get the ASCII art header
    header = generate_header()

    # Read the content of the imported_wallets.txt file
    with open("imported_wallets.txt", "r") as file:
        content = json.load(file)

    # Pass the header and content to the template
    return render_template('index.html', header=header, content=content)

@app.route('/run-scripts', methods=['POST'])
def start_cracking():
    # Start a new thread to run the script asynchronously
    threading.Thread(target=run_scripts).start()

    # Respond immediately to the client
    return 'Task started successfully. Refresh the page after completion.'

if __name__ == '__main__':
    socketio.run(app, debug=True)
