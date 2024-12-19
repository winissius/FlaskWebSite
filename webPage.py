from flask import Flask, render_template

app = Flask(__name__)

# first page
# route
# function

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contact")
def contact():
    return render_template("contacts.html")

# publish website
app.run(debug=True)