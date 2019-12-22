'''
2.Implement List comprehensions to produce the following listsWrite List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3
'''
###############################################
input_value = ['A','C','A','D','G','I','L']
list_comprehenssion = [ alphabet for alphabet in input_value ]
print(list_comprehenssion)

###############################################
input_string = "ACADGILD"
list_comprehenssion = [ alphabet for alphabet in input_string ]
print(list_comprehenssion)
###############################################
input_list=['x','y','z']
comp_list=[i*j for i in input_list for j in range (1,5)]
print(comp_list)

###############################################
input_list=['x','y','z']
my_list=[x*i for i in range(1,5) for x in input_list]
print(my_list)
##############################################
my_list=[2,3,4]
out_put=[[i+num] for i in my_list for num in range(0,3) ]
print(out_put)

###############################################

input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,3)]
print(result)

###############################################
input_list=[1,2,3]
out_put=[(j,i) for i in input_list for j in range(1,4)]
print(out_put)
