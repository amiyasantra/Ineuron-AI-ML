#3:Implement a function longestWord() that takes a list of words and returns the longest one

#######################(Own Reduce function to find longest word in given string)##########

def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

#########################(recursive Function to call by my_reduce method)#######

def longest_word_fun(first_word, second_word):              # Defining a methode name longest_word_fun and pussing  2 arguments 
    if(len(first_word)>len(second_word)):                   # checking length of given words taken through methode parameters
        return first_word                                   # returning word depending on condition
    else:
        return second_word                                  # returning word depending on condition
    
##########################(Main program)######################

user_input =input("Enter a string to check longest word: ") # Taking a input string from user
iput_converted_list=user_input.split()                      # convert string to list using .split() predefine methode
if(len(iput_converted_list)==0):                            # check conderted list is empty or not
    print("Your list is empty!kindly provied some value in input string!")  #Printing messages if list is empty

longest_word=reduce(longest_word_fun,iput_converted_list)   # calling my own reduce function to find longest word 
print(longest_word)                                         # printing the longest word
