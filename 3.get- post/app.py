from flask import Flask


# create name boject that represent our webpage
app=Flask(__name__)




@app.route("/")             # when a pertion visit home page thit is run automaticly
def home():
    return "Hello user! this is my first Flask app"

# run flask app :- open terminal and type flask run 
# close flask app :- ctrl + c


@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
def contact():
    return "This is contact page"


# GEt use for only read  POST use for right

from flask import request
@app.route("/submit",methods={"GET","POST"})
def submit():
    if request.method=="POST":
        return "To send data!"
    else:
        return "You are only view the form!"