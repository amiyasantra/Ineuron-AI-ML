'''
Problem Statement​ ​1:
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
'''

subject=["Americans", "Indians"]
verbs=["Play", "watch"]
objects=["Baseball","cricket"]

# Use list comprehension to print statement 3 for loop to generate list
sentence_list = [(sub+" "+ vrb + " " + obj) for sub in subject for vrb in verbs for obj in objects]
for sentence in sentence_list:
    print (sentence)
