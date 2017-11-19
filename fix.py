#This file will keep the class that I will use to fix the quotes from the API.

class Fix():

    #This method will specifically focus on getting rid of the <p> tag at the start of the quote. 
    def fix_paragraph_tag(self, content):
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
        return content, first

    #This method will basically delect the elements in the first and last positions. 
    def delete(self, content):
        #Since first gets pushed in the 0 position, I now need to delete the element that was in the 0 position
        #and is now in the 1 position
        last_value = content[-1]
        #Here I'm checking what the last value is 
        if last_value != '</p>':
            #I turn the last word, which contains the closing p tag, into a list
            last_value_list = list(last_value)
            #Find the location of the '<' part of the </p> tag
            first_value = last_value_list.index('<')
            #Finding the last part of the p tag, which is '>'
            last_value = first_value + 4
            #I then slice that part out of the list
            del last_value_list[first_value:last_value]
            #I rejoin all the letters from the list to make a string again
            word = ''.join(last_value_list)
            #insert the word into the last position of the content list
            content.insert(len(content), word)
            #Deleting the p tags
            del content[1]
            del content[-2]
        else:
            del content[1]
            del content[-1]
        #I then turn the elements in the list into a string 
        content = ' '.join(content)
        return content

