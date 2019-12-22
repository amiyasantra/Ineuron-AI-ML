'''
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
'''

##################(Method to map word to word length)#######
def word_length(list_words):
    return list(map(lambda x: len(x), list_words))


####################(main method)############################
word=input("Enter a string:")            # taking a input string from user
list_words=word.split()                  # creating a list from input string 
if(len(list_words)==0):                  # chcking input list is empty or not
    print("input list is empty kindly provide some value to it!")
else:
    print ("word lengths:::: " + str(word_length(list_words)))  # calling word_length function to map word to word_length
