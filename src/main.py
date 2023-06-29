from flask import Flask, render_template

import os
 
app = Flask(__name__)

def log(e):
    print("{0}\n".format(e))

global myvar
myvar = os.getenv('MYVAR', '{myvar not set}')
log("myvar = " + myvar)
 
# set up root route
@app.route("/")
def hello_world():
    message = "The environment variable is set to: " + myvar
    return render_template("index.html", msg=message)
 
# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
