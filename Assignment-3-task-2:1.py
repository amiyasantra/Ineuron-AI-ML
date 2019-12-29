'''
Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically, when
increasing is False, the i-th output column is the input vector raised element-wise to the power
of N - i - 1.
HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde
'''

import numpy as py  # iporting num py

#############defining mehod got genrate matrix#################
def generate_matrix(N,increasing=True):
    x=np.array([1,2,3,4])
    if increasing == True:
        np.vander(x,N,increasing=True)
        return np.column_stack([x**(N-i-1)for i in range(N)])
    if increasing == False:
        print("pass true as argumment to genrate matrix")
        

generate_matrix(int(input("enter number: ")),False) # calling function and passing argument to it
