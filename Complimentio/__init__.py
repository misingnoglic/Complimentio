from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random

account_sid = "AC66feb8a0982d83f73782a94069212ed7"
auth_token  = "34ddec2af3dad454914b40280328c820"
client = TwilioRestClient(account_sid, auth_token)

def messageparse(body):
    comps = ["Hey Sexy"]
    if " " in body:
        return [body[:body.index(" ")],body[body.index(" ")+1:]]
    else: return [body, comps[random.randint(0,len(comps))]]


def sendmessage(client, tonumber, compliment):
    message = client.messages.create(body=compliment,
        to=tonumber,
        from_="+16267747161",)
    #media_url="http://www.example.com/hearts.png")
    #print message.sid

 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    print(request.args['Body'])
    stuff = messageparse(str(request.args['Body']))
    sendmessage(client, stuff[0], stuff[1])
    resp = twilio.twiml.Response()
    resp.message("Thank You, your message has been sent")#request.args['Body']
    return str(resp)


 
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
