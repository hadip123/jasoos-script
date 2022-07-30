from flask import Flask, request
import os

app = Flask(__name__)

@app.route('all-process')
def all_process():
    return os.popen('wmic process get description, processid').read()

@app.route('kill')
def kill_process():
    process_name = request.args.get('processName')
    return os.popen('taskkill /IM ' + process_name + ' /F')
