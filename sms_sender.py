#!/usr/bin/python2
# coding: utf-8
import requests
import json
import sys

API_KEY=""

def read_config(config):
    try:
        f = open(config, "rb")
    except:
        sys.exit("{-} Opening config file failed!")
    data = f.read()
    try:
        config_data = json.loads(data)
        return config_data
    except:
        sys.exit("{-} JSON Parsing failure!")

def send_sms(message_config):
    victim = message_config['victim']
    sender = message_config['sender']
    message = message_config['message']
    print "{*} Sending '%s' to %s from %s" %(message, victim, sender)
    try:
        url = "https://api.clockworksms.com/http/send.aspx"
        data = {"key": API_KEY, "to": victim, "from": sender, "content": message}
        r = requests.get(url, data=data)
        print r.text
    except Exception, e:
        print e


def run(config):
    config_data = read_config(config)
    print "{+} Got %d tasks to run..." %(len(config_data))
    for x in range(0, len(config_data)):
        send_sms(message_config=config_data[x])

def main(args):
    if len(args) == 1:
        config = "spoof.json"
    else:
        config = args[1]
    print "{*} Using %s" %(config)
    run(config=config)

if __name__ == "__main__":
    main(args=sys.argv)
