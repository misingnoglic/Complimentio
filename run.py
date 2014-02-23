from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #here is what you would fill with the body of the text sent to twilio
    resp.message("Hello, Mobile Monkey")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)

def messageparse(body):
    if " " in body:
        return [body[:body.index(" ")],body[body.index(" ")+1:]]
    else: return [body]
