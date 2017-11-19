#This file will contain the connections to the MySQL database to store the amount of food 

#Importing files to use in this file.
import mysql.connector

class Food_Data():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3306,
                                database='market')
        self.cursor = self.conn.cursor()

    #This method will insert a food object into the database.
    def insert_food(self, food_list):
        count = 0
        while count < len(food_list):
            self._SQL = """insert into food_data
              (name, amount, profit)
              values
              (%s, %s, %s)"""
            self.cursor.execute(self._SQL, (food_list[count].name, food_list[count].amount, food_list[count].profit))
            self.conn.commit()
            count += 1

    #This method will pull one type of food from the database. 
    def pull_food(self):
        #This list will be used to do a query on all the food types. 
        foods = ['Kale', "Collards", "Spinach", 'Broccoli']
        #This list will hold all the data coming back from the database
        # food_data = []
        food_data = {}
        #A count variable to be used in the while loop
        count = 0
        while count < len(foods):
            #The query for the database 
            query = ("""SELECT * FROM food_data WHERE name = %s""")
            self.cursor.execute(query, (foods[count],))
            #A variable to hold the returning data
            row = self.cursor.fetchall()
            #Placing the food into the dictionary. 
            food_data[foods[count]] = row
            #The returned data is then placed into the food_info array
            # food_data.append(row)
            count += 1
        return food_data

    #This method will get the total pounds for each food and add it to a dictionary. 
    def get_pounds(self, food_data):
        #Setting up the pound dictionary. This will hold the 
        pound_data = {}
        #looping through the dictionary
        for key, value in food_data.items():
            count = 0
            total = 0
            #The second loop is to go through each array in the dictionary
            while count < len(food_data[key]):
                #Collecting the total for each array
                total = food_data[key][count][1] + total 
                count += 1
            #Using a dictionary which will hold the food type and total pounds sold off of it. 
            pound_data[key] = total
        #Returning the data
        return pound_data

    #This method will get the total pounds for all of the foods
    def total_pounds(self, pound_data):
        total = 0
        for key, value in pound_data.items():
            total = value + total
        return total 

    #This method will get the total profit for each food and add it to a dictionary
    def get_profit(self, food_data):
        profit_data = {}
        for key, value in food_data.items():
            count = 0
            total = 0
            while count < len(food_data[key]):
                total = food_data[key][count][2] + total 
                count += 1
            profit_data[key] = total 
        return profit_data

    #This method will get the total profit for all of the foods 
    def total_profit(self, profit_data):
        total = 0
        for key, value in profit_data.items():
            total = value + total
        return total 

        
