#!/usr/bin/env python

import argparse
from requestHelper import RequestHelper
import time

parser = argparse.ArgumentParser()
parser.add_argument("action", help="Please specify the action")
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()
action = args.action
key = args.key
value = args.value

requestHelper = RequestHelper()

if action == "set":

    if requestHelper.keyExists(key):
        print "Key Already exists, Updating..."
        requestHelper.update(key, value)
    else:
        print "Inserting .."
        requestHelper.post(key, value)

elif action == "get":
    print "Fetching Values..."
    requestHelper.fetch(args.key)

elif action == "watch":
    print "Watching the Data Store"
    while 1:
        requestHelper.fetch("all")
        time.sleep(2)
