'''
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
a vowel, False otherwise.
'''
####################(method to check char is vowel and return True/False)############################
def vowel_check(char):
    
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        
        return True
    else:
        return False
#######################(Main methode)################################
char = input("Enter character: "); # Take user input
if (char.isalpha() == False):      # If Invalid input, exit
    exit();
if (vowel_check(char)): # calling vowel_check methode to check alphabtl is  vowel or not
    print(char, "is a vowel.");
else:
    print(char, "is not a vowel."); 
