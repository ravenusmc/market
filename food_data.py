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
        food_data = []
        #A count variable to be used in the while loop
        count = 0
        while count < len(foods):
            #The query for the database 
            query = ("""SELECT * FROM food_data WHERE name = %s""")
            self.cursor.execute(query, (foods[count],))
            #A variable to hold the returning data
            row = self.cursor.fetchall()
            #The returned data is then placed into the food_info array
            food_data.append(row)
            count += 1
        return food_data

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
        

# test = Food_Data()
# test.pull_food()
#print(row[1][2])


# Scrap Code 

# print(food_data)
#print(food_data[0][0][1])


# This will loop through the food object
# use if then statement based on counter to assign values with it reaching 2 to insert!
# for attr, value in food.__dict__.items():
#     food_name = value
#     amount = value
#     cost = value
#     self._SQL = """insert into food
#         (name, username, password)
#     values (%s, %s, %s)"""
#     self.cursor.execute(self._SQL, (food_name, amount, cost))
#     self.conn.commit()
#     print(value)

# for attr, value in food.__dict__.items():
# if count == 0:
#     food_name = value
#     print(food_name)
# if count == 1:
#     amount = value
#     print(amount)