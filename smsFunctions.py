import os
import twilio
from twilio.rest import Client

account_sid = os.environ['ACf3da6c862b2b0b546088c178c6354a14']

account_authtoken = os.environ['14bcdabb1d104fbf8acdfca27e35df3c']
client = Client(accout_sid, account_authtoken)


def sendMsg(msg, reciepient):
    message = client.messages \
    .create(
        body = msg,
        from_ = +12055573376,
        to = reciepient
    )
    return message



# TESTING
sendSMS("Testing", 9786210713)


