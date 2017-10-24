#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import json 
import requests

#importing files I made for this project
from food import *
from food_data import *
from quote import *
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
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            if not_found:
                flash('Username not found, maybe sign up!')
            elif password_no_match:
                flash('Password does not match! Maybe sign up!')
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
@app.route('/home', methods=['GET', 'POST'])
def home():
    #This session will prevent users who have not signed up from coming in.
    if 'username' not in session:
        return redirect(url_for('signup'))
    #This method fires when the user hits the submit button. 
    if request.method == 'POST':
        #Creating a food object
        food = Food()
        #Calling the get_food method which will set food amounts for each type of food. 
        food_list = food.get_Food()
        #Creating the food data object to insert food into the database
        data = Food_Data()
        data.insert_food(food_list)
    username = session['username']
    #Creating a list to hold the quotes
    quotes = []
    #Setting up the quote object
    quote = Quote()
    #Getting the response from my quote api
    response = quote.getting_quotes()
    #parsing out the data that I need-the actual quotes
    quotes = quote.get_data(response)
    return render_template('home.html', name = username, quotes = quotes)

#This route will take the user to the stats page
@app.route('/stats', methods=['GET', "POST"])
def stats():
    #I will be using his list of the foods for reference throughout the stats page
    foods = ['Kale', 'Collards', 'Broccoli', 'Spinach']
    #Creating a food object
    food = Food_Data()
    #Calling the pull_food method which will pull the data out of the database
    food_data = food.pull_food()
    #I then use the get_poundage method to get the total pounds for all the food
    total_pounds = food.get_poundage(food_data)
    #I turn the two lists, foods and total_pounds into a dictionary
    pound_dictionary = dict(zip(foods, total_pounds))

    #poundData = json.dumps(pound_dictionary, ensure_ascii=False)

    total_profit = food.get_profit(food_data)
    profit_dictionary = dict(zip(foods, total_profit))
    return render_template('stats.html', pounds=pound_dictionary, profit=profit_dictionary)


#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    #Redirect to Landing page
    return redirect(url_for('landing'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)

#Scrap code 