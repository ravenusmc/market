#This file will deal with the post methods for when the amount of food is submitted

from flask import request

#This class will deal with the amount of food that comes in. 
class Food():

    #Here I describe all the properties that each Food object will have
    def __init__(self):
        self.name = ""
        self.amount = 0
        self.profit = 0

    #This method will set the food amounts when the user submits the form
    def get_Food(self):
        food_list = []
        #Here I'm receiving the values from the form that the user entered. 
        kale = request.form['kale_amount']
        collards = request.form['collard_amount']
        broccoli = request.form['broccoli_amount']
        spinach = request.form['spinach_amount']
        #These coditional statements get the information for the amount of food. 
        if kale:
            #Creating the food object
            kale_object = Food()
            #setting the name of the food object
            kale_object.name = "Kale"
            #setting the amount of pounds of the food object
            kale_object.amount = kale
            #Setting the specific profi earned based off poundage to the food object
            kale_object.profit = int(kale) * 2
            #Appending all the data to the food list which will hold each type of food object. 
            food_list.append(kale_object)
        if collards:
            collards_object = Food()
            collards_object.name = "Collards"
            collards_object.amount = collards
            collards_object.profit = int(collards) * 3
            food_list.append(collards_object)
        if broccoli:
            broccoli_object = Food()
            broccoli_object.name = 'Broccoli'
            broccoli_object.amount = broccoli
            broccoli_object.profit =  int(broccoli) * 4
            food_list.append(broccoli_object)
        if spinach:
            spinach_object = Food()
            spinach_object.name = 'Spinach'
            spinach_object.amount = spinach
            spinach_object.profit = int(spinach) * 5
            food_list.append(spinach_object)
        return food_list

