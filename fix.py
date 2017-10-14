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
        del content[1]
        del content[-1]
        #I then turn the elements in the list into a string 
        content = ' '.join(content)
        return content

