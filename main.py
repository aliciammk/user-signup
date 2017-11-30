from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if len(username) < 3 or len(username) > 20:
        username_error = "Please enter a username between 3 and 20 characters long."
        return redirect("/?error=" + username_error)
    
    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters long."
        return redirect("/?error=" + password_error)
    
    if password != verify:
        verify_error = "Passwords do not match."
        return redirect("/?error=" + verify_error)
    
    if len(email)> 0 and "." not in email and "@" not in email:
        email_error = "Email is not valid."
        return redirect("/?error=" + email_error)

    else:
        return render_template('welcome.html', username=username)


@app.route("/welcome", methods=['POST'])

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()