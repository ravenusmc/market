#This file will deal with the quote api to bring up random quotes each time the program is used. 

#importing libraries to use
import requests

class Quote():

    def __init__(self):
        self.__url = "http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=3"

    #This method will get the quotes from the quote API. 
    def getting_quotes(self):
        #Getting the response
        response = requests.get(self.__url)
        response_dict = response.json()
        #print(response_dict[0]['content'])
        return response_dict

    #This method will pull the data that I need out of the respones
    def get_data(self, quotes):
        #Setting up a counter 
        count = 0 
        #This list will hold the quote that I need from the dictionary.
        content = []
        while count < 3:
            content.append(quotes[count]['content'])
            count += 1 
        return content

        # print(quotes[0]['content'])


# quote = Quote()
# response = quote.getting_quotes()
# quote.get_data(response)