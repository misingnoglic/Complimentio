from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])

def messageparse(body):
	comps = ["Hey Sexy"]
    if " " in body:
        return [body[:body.index(" ")],body[body.index(" ")+1:]]
    else: return [body, comps[random.rantint(0,len(comps))]]


def sendmessage(client, tonumber, compliment):
    message = client.messages.create(body=compliment,
        to=tonumber,
        from_="+16267747161",)
    #media_url="http://www.example.com/hearts.png")
    print message.sid


account_sid = "AC66feb8a0982d83f73782a94069212ed7"
auth_token  = "34ddec2af3dad454914b40280328c820"
client = TwilioRestClient(account_sid, auth_token)

textbody = messageparse(somemessage.body)
sendmessage(client, "3233933245", textbody[1])
#not aryas # but we're going to use his # to keep checking
 
if __name__ == "__main__":
    app.run(debug=True)