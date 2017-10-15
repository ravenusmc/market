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
    def insert_food(self, food):
        self._SQL = """insert into food
          (name, username, password)
          values
          (%s, %s, %s)"""
        self.cursor.execute(self._SQL, (name, username, hashed))
        self.conn.commit()

        #This will loop through the food object
        # for attr, value in food.__dict__.items():
        #     print(value)