import os
import twilio
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
account_authtoken = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, account_authtoken)


def send_msg(msg, reciepient):
    message = client.messages \
    .create(
        body = msg,
        from_ = '+12055573376',
        to = reciepient
    )
    return message



# TESTING
send_msg("testing", '9786210713')


