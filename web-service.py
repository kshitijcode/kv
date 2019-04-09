#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

db = {}


class SetKeyValueStore(Resource):

    def post(self):
        global db
        data = request.get_json()
        db[data['key']] = data['value']
        return {"Inserted Value ": "Key --> " + data['key'] + " and Value --> " + data['value']}, 201

    def put(self):
        data = request.get_json()
        db[data['key']] = data['value']
        return {"Updated Value ": "Key --> " + data['key'] + " and Value --> " + data['value']}, 201


class GetValueFromStore(Resource):

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

if __name__ == "__main__":
    app.run(debug=True)
