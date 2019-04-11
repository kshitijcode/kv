#!/usr/bin/env python
import requests
import urlparse
import socketio
import constants


class RequestHelper:

    def __init__(self):
        # Helper Class to Interact with the Web Service using Requests Module
        pass

    def keyExists(self, key):

        # Check if the key exists in DB
        r = requests.get(constants.ENDPOINT + "fetch/" + key)

        if r.status_code != 200:
            return False

        return True

    def fetch(self, key):
        r = requests.get(constants.ENDPOINT + "fetch/" + key)
        print r.content

    def post(self, key, value):
        r = requests.post(urlparse.urljoin(constants.ENDPOINT, "set"), json={"key": key, "value": value},
                          headers=constants.HEADERS)
        print r.content

    def update(self, key, value):
        r = requests.put(urlparse.urljoin(constants.ENDPOINT, "set"), json={"key": key, "value": value},
                         headers=constants.HEADERS)
        print r.content

    def watch(self, key):
        r = requests.get(constants.ENDPOINT + "fetch/" + key)
        print r.content

    def connectSocket(self):
        sio = socketio.Client()
        sio.connect(constants.ENDPOINT)

        @sio.on('value_update')
        def on_message(data):
            print("Recently Added Value is" + str(data))