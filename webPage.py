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

@app.route("/users/<username>")
def users(username):
    return render_template("users.html", username=username)

# publish website
app.run(debug=True)