import textwrap
import re
mystring = 'This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.'
page_wrap_by = 25
mylist = textwrap.wrap(mystring,page_wrap_by)

def string_count(input_list):
        n = 0
        for i in input_list:
            n = n + len(i)
        return n

for i in range(0, len(mylist)):
          list_of_mylist = list(mylist[i])
          current_char_length = len(list_of_mylist)
          spaces_to_add=page_wrap_by - current_char_length
          current_space_count = len([x for x in list_of_mylist if x == ' '])
          for j,x in enumerate(list_of_mylist):
              if (x == ' ') and (string_count(list_of_mylist) < page_wrap_by):
                  list_of_mylist.insert(j+1, ' ')
          final_list = ''.join(list_of_mylist)
          print(final_list)
