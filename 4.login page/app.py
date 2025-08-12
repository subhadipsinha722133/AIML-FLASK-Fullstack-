from flask import Flask, request, redirect, url_for, session, Response

# create name object that represent our webpage
app = Flask(__name__)

# when we are work in session 
app.secret_key = "supersecretkey"

# login home page - both GET and POST methods
@app.route("/", methods=["GET", "POST"])
def login():  # Changed from 'submit' to 'login' for clarity
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username    # store in session
            return redirect(url_for("wellcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype="text/plain")
    
    return '''                 
            <h2>Login Page</h2>
            <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="Login">
            </form>
           '''

@app.route("/wellcome")
def wellcome():
    if "user" in session:
        return f"""
            <h2>Welcome, {session['user']}!</h2>
            <a href={url_for('logout')}>Logout</a>
           """
    return redirect(url_for("login"))  # Now this will work

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))  # Now this will work

if __name__ == "__main__":
    app.run(debug=True)