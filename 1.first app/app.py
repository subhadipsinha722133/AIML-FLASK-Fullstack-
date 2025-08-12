from flask import Flask


# create name boject that represent our webpage
app=Flask(__name__)




@app.route("/")             # when a pertion visit home page thit is run automaticly
def home():
    return "Hello user! this is my first Flask app"

# run flask app :- open terminal and type flask run 
# close flask app :- ctrl + c