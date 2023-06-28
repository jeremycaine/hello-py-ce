from flask import Flask
import os
 
app = Flask(__name__)

global myvar
myvar = os.getenv('MYVAR', '{myvar not set}')

def log(e):
    print("{0}\n".format(e))
 
# set up root route
@app.route("/")
def hello_world():
    log("myvar = " + myvar)
    message = "Hello world and the message is " + myvar
    return message
 
# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(port))
