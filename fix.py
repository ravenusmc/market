#This file will keep the class that I will use to fix the quotes from the API.

class Fix():

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

    def delete(self, content):
        del content[1]
        del content[-1]

