from flask import Flask, render_template
from flask_socketio import SocketIO, send
#pip install python-socketio flask-socketio simple-websocket

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def ger_message(mensagem):
    send(mensagem, broadcast=True)

# Criar a primeira pagina
@app.route("/")
def homepage():
    return render_template("homepage2.html")

# roda o aplicativo
if __name__ == '__main__':
    socketio.run(app, host="10.0.0.208")