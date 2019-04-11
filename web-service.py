#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Initializing Empty DB
db = {}
isConnected = False


class SetKeyValueStore(Resource):

    # API Handler for Setting up Values
    def post(self):
        global db
        data = request.get_json()
        db[data['key']] = data['value']
        global isConnected
        if isConnected:
            socketio.emit("value_update", data)
        return {"Inserted Value ": "Key --> " + data['key'] + " and Value --> " + data['value']}, 201

    def put(self):
        data = request.get_json()
        db[data['key']] = data['value']
        global isConnected
        if isConnected:
            socketio.emit("value_update", data)
        return {"Updated Value ": "Key --> " + data['key'] + " and Value --> " + data['value']}, 201


class GetValueFromStore(Resource):

    # API Handler for Fetching Values
    def get(self, key):

        global db

        if key == "all":
            return {"Key Store State is ": db}

        if key in db.keys():
            return {"Value": db[key]}, 200
        else:
            return {"Error": "Key Not Found "}, 404


api.add_resource(SetKeyValueStore, '/set')
api.add_resource(GetValueFromStore, '/fetch/<key>')


@socketio.on('connect')
def connect():
    global isConnected
    isConnected = True


@socketio.on('disconnect')
def connect():
    global isConnected
    isConnected = False


if __name__ == "__main__":
    socketio.run(app)
    app.run(debug=True)
