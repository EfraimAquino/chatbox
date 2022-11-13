from flask import Flask, render_template
from flask_socketio import SocketIO, send
print('hi')
app = Flask(__name__)
app.config['SECRET'] = "secret123"
socketio = SocketIO(app, cors_allowed_orgins=[])


@socketio.on('message')
def handle_message(message):
    print("Received message:" + message)
    if message != "User Connected!":
        send(message, broadcast = True)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host = "0.0.0.0", port= 2356)