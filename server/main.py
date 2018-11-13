#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/documentation')
def show_documentation():
    return render_template("documentation.html")

@socketio.on("code")
def handle_message(code):
    print("received code",code)
    message = "There is an action pending for:" + code['data']
    d = code['data']

    emit("news", d, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)
