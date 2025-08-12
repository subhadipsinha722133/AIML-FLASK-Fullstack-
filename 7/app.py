from flask import Flask,render_template,request


app=Flask(__name__)

@app.route("/")             
def login():
    return render_template("login.html")

@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")


    # if username=="khokon" and password=="123":
    #     return render_template("walcome.html",name=username)

    valid_users={
        'admin':'123',
        'khokon':'pass1',
        'sinha':'pass2'
    }
    if username in valid_users and password==valid_users[username]:
        return render_template("walcome.html",name=username)
    
    else:
        return "invaliv name or password"
    
