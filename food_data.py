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
            
            count += 1
            # self._SQL = """insert into food
            #   (name, username, password)
            #   values
            #   (%s, %s, %s)"""
            # self.cursor.execute(self._SQL, (name, username, hashed))
            # self.conn.commit()


#Scrap Code 
#This will loop through the food object
#use if then statement based on counter to assign values with it reaching 2 to insert!
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

for attr, value in food.__dict__.items():
if count == 0:
    food_name = value
    print(food_name)
if count == 1:
    amount = value
    print(amount)