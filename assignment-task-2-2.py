#Create the below pattern using nested for loop in Python.
#	*
#	**
#	***
#	****
#	***
#	**
#	*

number = input("Enter a number to print above pattren: ") # taking a integer number from user to create above pattren 
if (number.isdigit()):                             # validating user input is a number
    for i in range(0, int(number)):                # define a for loop from 0 to value of input number in intiger
        for j in range(0, i+1): print("* ",end="") # define a nested for loop and printing number of start in every row depending on value of n 
        print("\n")                                # after for loop provide a new line space
    for i in range(int(number)-1,0,-1):            # define a for loop from 0 to value of number-1 to print exact pattarn
        for j in range(0,i): print("* ",end="")    # define a nested for loop and printing number of start in every row depending on value of n 
        print("\n")                                # after for loop provide a new line space
        
else:
    print("enter a intiger number!")
