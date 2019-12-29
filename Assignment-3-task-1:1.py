'''
Problem Statement:
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

################Methode to generate exception devide by zero excepetion#############
def div_by_zero():
    return 5/0

try:
    div_by_zero()
except ZeroDivisionError as exception:
     print("Handle run-time 'div by 0'error:", exception)
