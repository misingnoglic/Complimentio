# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
def messageparse(body):
    if " " in body:
        return [body[:body.index(" ")],body[body.index(" ")+1:]]
    else: return [body]


def sendmessage(client, tonumber, compliment):
    message = client.messages.create(body=compliment,
        to=tonumber,
        from_="+16267747161",)
    #media_url="http://www.example.com/hearts.png")
    print message.sid


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC66feb8a0982d83f73782a94069212ed7"
auth_token  = "34ddec2af3dad454914b40280328c820"
client = TwilioRestClient(account_sid, auth_token)
textbody = messageparse(somemessage.body)
sendmessage(client, "3233933245", textbody[1])
#not aryas # but we're going to use his # to keep checking