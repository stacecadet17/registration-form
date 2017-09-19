from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'pocketfullofsunshine'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/results', methods = ['POST'])
def results():
    #Email
    if len(request.form['email']) < 1:
        flash("email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email!")

    #First Name
    if len(request.form['first_name']) < 1:
        flash("field cannot be empty!")
    elif not (request.form['first_name']).isalpha():
        flash("name must only contain letters!")

    #Last Name
    if len(request.form['last_name']) < 1:
        flash("field cannot be empty!")
    elif not (request.form['last_name']).isalpha():
        flash("name must only contain letters!")

    #Password
    if len(request.form['password']) < 1:
        flash("field cannot be empty!")
    elif len(request.form['password']) < 8:
        flash("password is too short!")


    #Confirm Password
    if len(request.form['confirm_password']) < 1:
        flash("Field cannot be empty!")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Passwords do not match!")

    else:
        return render_template('result.html', firstname = session['first_name'], lastname = session['last_name'], password = session['password'], confirmpassword = session['confirm_password'] )
    return redirect('/')



app.run(debug=True)
