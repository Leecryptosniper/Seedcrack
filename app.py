# app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO
import subprocess
import threading
import os  # Import the os module

app = Flask(__name__)
socketio = SocketIO(app)

def run_scripts():
    # Code to execute the run_scripts.bat script
    subprocess.run(['run_scripts.bat'])

    # Notify the client that the script has completed
    socketio.emit('script_completed', {'status': 'success'})

@app.route('/')
def index():
    # Read the content of the imported_wallets.txt file
    with open("imported_wallets.txt", "r") as file:
        content = file.read()

    # Pass the content to the template
    return render_template('index.html', content=content)

@app.route('/run-scripts', methods=['POST'])
def start_cracking():
    # Start a new thread to run the script asynchronously
    threading.Thread(target=run_scripts).start()

    # Respond immediately to the client
    return 'Task started successfully. Refresh the page after completion.'

if __name__ == '__main__':
    socketio.run(app, debug=True)
