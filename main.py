#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the landing page
@app.route('/', methods=['GET', 'POST'])
def landing():
  if request.method == 'POST':
    #Recieving the information from the user.
    username = request.form['username']
    password = request.form['password']
  return render_template('login.html')

#This route takes the user to the signup page
@app.route('/signup')
def signup():
  return render_template('signup.html')



# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)