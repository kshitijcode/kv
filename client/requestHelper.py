#!/usr/bin/env python
import requests
import urlparse
import constants


class RequestHelper:

    def __init__(self):
        pass

    def keyExists(self, key):
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
