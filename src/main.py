from flask import Flask, render_template

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
    message = "The environment variable is set to: " + myvar

    return render_template("index.html", msg=message)
 
# Get the PORT from environment
port = os.getenv('PORT', '8080')
debug = os.getenv('DEBUG', 'False')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=debug)
