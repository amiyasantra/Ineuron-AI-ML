#1.2 Write a Python program to implemenPython's built-in function filter

#########################(my filter methode)######################
def my_filter(func,sequence):
    res=[]
    for variable in sequence :
        if func(variable):
            res.append(variable)
    return res
########################(validating my filter using is_even function methode)###########
def is_even(item):
    if item%2==0 :
        return True
    else :
        return False
#########################check myfilter function#####################
seq=[1,2,3,4,5,6,7,8,9,10]
print(my_filter(is_even,seq))
