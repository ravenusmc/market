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
        quote_list = []
        while count < 3:
            #Here I get the specific quote
            content = quotes[count]['content']
            print(content)
            #I then put the quote into a list with each word being an element in the list.
            content = content.split()
            #I then get the first element in the list which will have the first html tag. 
            first = content[0]
            #I take that word and break it up into a list 
            first = list(first)
            tag_count = 0
            while tag_count < 3:
                del first[0]
                tag_count += 1
            #Using join method to bring the individual letters back into a word. 
            first = ''.join(first)
            #I need to push first back into first spot in the content string.
            content.insert(0, first)
            #Since first gets pushed in the 0 position, I now need to delete the element that was in the 0 position
            #and is now in the 1 position
            del content[1]
            del content[-1]
            #I then turn the elements in the list into a string 
            content = ' '.join(content)
            quote_list.append(content)
            count += 1 
            print(quote_list)
            input()
        return quote_list

        # print(quotes[0]['content'])


quote = Quote()
response = quote.getting_quotes()
quote.get_data(response)

# In [9]: a = list(range(10))
# In [10]: a
# Out[10]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# In [11]: del a[-1]
# In [12]: a
# Out[12]: [0, 1, 2, 3, 4, 5, 6, 7, 8]