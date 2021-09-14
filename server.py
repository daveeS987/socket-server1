# to run locally enter the following into terminal
# gunicorn -k eventlet -w 1 --reload server:app
# ----------------------------------
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("A new user Connected: ", sid)


@sio.event
def message(sid, data):
    print("Message from client: ", data)


@sio.event
def disconnect(sid):
    print("Disconnected SID >> ", sid)
