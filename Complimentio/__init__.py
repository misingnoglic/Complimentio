from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random

account_sid = "AC66feb8a0982d83f73782a94069212ed7"
auth_token  = "34ddec2af3dad454914b40280328c820"
client = TwilioRestClient(account_sid, auth_token)



def messageparse(body):
    if " " in body:
        stuff= [body[:body.index(" ")],body[body.index(" ")+1:]]
        if stuff[1] == "*fun":
            f = open("funnylist.txt","r")
            comps = eval(f.read())
            stuff= [body[:body.index(" ")], comps[random.randint(0,len(comps))-1]]

    else:
        f = open("reglist.txt","r")
        comps = eval(f.read())
        stuff= [body, comps[random.randint(0,len(comps))-1]]
    return stuff


def sendmessage(client, tonumber, compliment):
    Msg = "Hello, you have been sent an anonymous compliment: "
    message = client.messages.create(body=Msg+compliment,
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
    if stuff[0].isdigit() and (len(stuff[0])>8 and len(stuff[0])<12):
        sendmessage(client, stuff[0], stuff[1])
        msg = "Thank You, your message has been sent"
    else: msg = "Please enter a 9-11 digit phone number (with no spaces) followed by a compliment. If you don't enter a compliment one will be chosen for you"
    resp = twilio.twiml.Response()
    resp.message(msg)#request.args['Body']
    return str(resp)


 
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)


