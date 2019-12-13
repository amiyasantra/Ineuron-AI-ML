#   Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#   of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#   comma-separated sequence on a single line

# Methode-1
start=2000
end=3200
mylist = []                  # defining a list mylist[]
for i in range(start,end+1): # run a loop from 2000 to 3210
    if i%7==0 and i%5!=0:    # checking number is divisibleby 7 and not multiple of 5
       mylist.append(str(i)) # appending numbers which are divisibleby 7 but not multiple of 5
print ("Numbers which are divisible by 7 but not multiple of 5\n")
print (','.join(mylist))     # printing numbers from list

# Methode-2
start=2000
end=3200
for i in range (start,end+1): # run a loop from 2000 to 3210
    if i%7==0 and i%5!=0:   # checking number is divisibleby 7 and not multiple of 5
        print(i,end=",")    # printing numbers which are divisible by 7 but not multiple of 5
        
