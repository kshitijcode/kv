#!/usr/bin/env python

import argparse
from requestHelper import RequestHelper

# Parsing values from CLI
parser = argparse.ArgumentParser()
parser.add_argument("action", help="Please specify the action")
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

# Fetching necessary values
action = args.action
key = args.key
value = args.value

requestHelper = RequestHelper()

# Take appropriate method call based upon action variable based from CLI
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
    requestHelper.connectSocket()