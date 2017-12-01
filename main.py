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

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        error = "Please enter a valid username."
        error_type = "username_error"
        return render_template('signup.html', password='', verify='', email=email, error=error, error_type=error_type)
    
    elif len(password) < 3 or len(password) > 20:
        error = "Please enter a valid password."
        error_type = "password_error"
        return render_template('signup.html', username=username, password='', verify='', email=email, error=error, error_type=error_type)
    
    elif password != verify:
        error = "Passwords do not match."
        error_type = "verify_error"
        return render_template('signup.html', username=username, password='', verify='', email=email, error=error, error_type=error_type)
    
    elif len(email)> 0 and "." not in email and "@" not in email:
        error = "Email is not valid."
        error_type = "email_error"
        return render_template('signup.html', username=username, password='', verify='', error=error, error_type=error_type)

    else:
        return render_template('welcome.html', username=username)


@app.route("/welcome", methods=['POST'])

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    error_type = request.args.get("error_type")
    return render_template('signup.html', error=encoded_error and cgi.escape(encoded_error, quote=True), error_type=error_type and cgi.escape(error_type, quote=True))

app.run()