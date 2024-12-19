from flask import Flask

app = Flask(__name__)

# first page
# route
# function

@app.route("/")
def homepage():
    return "hello world"

# publish website
app.run()