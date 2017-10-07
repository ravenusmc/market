#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#importing files I made for this project
from user import *

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the landing page
@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        #Recieving the information from the user.
        username = request.form['username']
        password = request.form['password']
        #Creating a user object
        user = User()
        #Checking to see if the user is in the database.
        flag, not_found, password_no_match = user.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('home'))
    return render_template('login.html')

#This route takes the user to the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        #Creating the user object
        user = User()
        #Encrypting the password
        password, hashed = user.encrypt_pass(password)
        #Adding the user to the database
        user.insert(name, username, hashed)
        #Letting them into the index Page
        return redirect(url_for('home'))
    return render_template('signup.html')

#This route takes the user to the home page
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('signup'))
    return render_template('home.html')


#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('landing'))



# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)