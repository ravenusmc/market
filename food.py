#This file will deal with the post methods for when the amount of food is submitted

from flask import request

#This class will deal with the amount of food that comes in. 
class Food():

    def __init__(self):
        self.kale = "Kale"
        self.kale_amount = 0
        self.collards = "Collards"
        self.collard_amount = 0
        self.broccoli = "Broccoli"
        self.broccoli_amount = 0
        self.spinach = "Spinach"
        self.spinach_amount = 0 

    def get_Food(self):
        if request.form.get('Kale'):
            self.kale_amount = request.form['kale_amount']
        if request.form.get('Collards'):
            self.collard_amount = request.form['collard_amount']
        if request.form.get('Broccoli'):
            self.broccoli_amount = request.form['broccoli_amount']
        if request.form.get('Spinach'):
            self.spinach_amount = request.form['spinach_amount']






#Scrap code -Code that I was using then realized that I do not need it but keep it around 'just in case'

# if request.form.get('Kale') and request.form.get('Collards') and request.form.get('Broccoli') and request.form.get('Spinach'):
#     self.kale_amount = request.form['kale_amount']
#     self.collard_amount = request.form['collard_amount']
#     self.broccoli_amount = request.form['broccoli_amount']
#     self.spinach_amount = request.form['spinach_amount']