# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

while True:                                  #running a loop check name is in alphabet or not
    Firstname = input("Enter First name\n")  # getting first name from user
    if Firstname.isalpha():                  # check first name is in alphabet or not
      Lastname = input("Enter Last name\n")  # getting last name from user
      if Lastname.isalpha():                 # check last name is in alphabet or not
        break
    print("Please enter characters A-Z only\n") # print the error message if names are not in alphabet 
print(Lastname+" "+Firstname)                   # print name in reverse order
print(Firstname[-1::-1]+" "+Lastname[-1::-1])   # print name in reverse order with later

