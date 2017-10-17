#This file will deal with the post methods for when the amount of food is submitted

from flask import request

#This class will deal with the amount of food that comes in. 
class Food():

    #Here I describe all the properties that each Food object will have
    def __init__(self):
        self.name = ""
        self.amount = 0
        # self.kale = ""
        # self.kale_amount = 0
        # self.collards = ""
        # self.collard_amount = 0
        # self.broccoli = ""
        # self.broccoli_amount = 0
        # self.spinach = ""
        # self.spinach_amount = 0 

    #This method will set the food amounts when the user submits the form
    def get_Food(self):
        if request.form.get('Kale'):
            kale = Food()
            kale.name = "Kale"
            kale.amount = request.form['kale_amount']
            print(kale.name)
            print(kale.amount)
        if request.form.get('Collards'):
            collards = Food()
            collards.name = "Collards"
            collards.amount = request.form['collard_amount']
            print(collards.name)
            print(collards.amount)
        if request.form.get('Broccoli'):
            self.Broccoli = "Broccoli"
            self.broccoli_amount = request.form['broccoli_amount']
        if request.form.get('Spinach'):
            self.Spinach = "Spinach"
            self.spinach_amount = request.form['spinach_amount']






#Scrap code -Code that I was using then realized that I do not need it but keep it around 'just in case'

# if request.form.get('Kale') and request.form.get('Collards') and request.form.get('Broccoli') and request.form.get('Spinach'):
#     self.kale_amount = request.form['kale_amount']
#     self.collard_amount = request.form['collard_amount']
#     self.broccoli_amount = request.form['broccoli_amount']
#     self.spinach_amount = request.form['spinach_amount']