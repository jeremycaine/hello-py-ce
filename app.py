import flask
import os
 
app = flask.Flask(__name__)

myvar = os.getenv('MYVAR', '<not set>')
print (myvar)
 
# set up root route
@app.route("/")
def hello_world():
    message = "Hello world and the message is " + myvar
    return message
 
# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(port))
