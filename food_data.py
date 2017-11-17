#This file will contain tthe connections to the MySQL database to store the amount of food 

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
        print(food_list[0].name)
        input()
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

    
    def get_pounds():


    #This method will get the pounds of all the different foods
    def get_poundage(self, food_data):
        #Counter to keep track of the while loop
        count = 0
        #This list will hold the total pounds for each type of food
        total_pounds = []
        #The first while loop will loop through the food_data list
        while count < len(food_data):
            inner_count = 0;
            total = 0
            #Second while loop will loop through each individual type of food
            while inner_count < len(food_data[count]):
                total = food_data[count][inner_count][1] + total
                inner_count += 1
            #Appending the total to the total pounds list
            total_pounds.append(total)
            count += 1
        #Returning the data
        return total_pounds

    #This method will get the total pounds that have been sold 
    def get_total_pounds_all_foods(self, total_pounds):
        total = 0
        count = 0
        while count < len(total_pounds):
            total = total_pounds[count] + total
            count += 1
        return total

    #This method will get the profits of all the different foods
    def get_profit(self, food_data):
        count = 0
        total_profits = []
        while count < len(food_data):
            inner_count = 0;
            total = 0
            while inner_count < len(food_data[count]):
                total = food_data[count][inner_count][2] + total
                inner_count += 1
            total_profits.append(total)
            count += 1
        return total_profits

    #This method will get the total dollar amount of food that has been sold 
    def get_total_profit_all_foods(self, total_profit):
        total = 0
        count = 0
        while count < len(total_profit):
            total = total_profit[count] + total
            count += 1
        return total

        
