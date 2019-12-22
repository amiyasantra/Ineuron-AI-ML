#Write a function filter_long_words() that takes a list of words and an integer n and returns the list
#of words that are longer than n.

#########################(user define methode)######################
def find_words(list_words,integer):      # define a methode to find word length grater then provided length
    return list(filter(lambda word:len(word)>integer,list_words)) # using lambda function to find list of word grater the integer value

##########################(main methode)##########################
word=input("Enter a string:")            # taking a input string from user
integer=int((input("enter an integer value to find word length grater then this "))) # taking a integer from user
list_words=word.split()                  # creating a list from input string 

if(len(list_words)==0):                  # chcking input list is empty or not
    print("input list is empty kindly provide some value to it!")
else:
    print(find_words(list_words,integer)) # calling find_words function to to find list of word grater then provided length  

