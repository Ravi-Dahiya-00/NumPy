import numpy as np 

# now we will create a numpy nd-arrays object 
# the array object in numpy is called nd-array.   array()


x=np.array([1,2,3,4,5])
print(x)
print(type(x))


# we can also pass a list , tuple or any array like object with array() and it will be converted to nd-array.

y=np.array((1,2,3,4,5))
print(y)
print(type(y))



# dimensions in array -->
'''                  a dimension in array is one level of array depth (nested array) '''


# O_d Arrays --> scalars,are the elements in an array , each value in an array is a 0-D array.

zero_D=np.array(42)
print(zero_D)


# 1-D arrays --> an array has 0-D arrays as its elements is called unidirectional or 1-D. 

one_D=np.array([1,2,3,4,5])
print(one_D)


# create a 2-D array containing 2 arrays with certain values 

two_D=np.array([[1,2,3],[4,5,6]])
print(two_D,"\n")



# create a 3-D array with two 2-D array

three_D=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(three_D)



# check the dimension of any array :  ndim attribute 

print(zero_D.ndim)
print(one_D.ndim)
print(two_D.ndim)
print(three_D.ndim)


# creating an array with 5 - D and verifying its dimensions

five_D=np.array([1,2,3,4,5],ndmin=5)

print(five_D)
print(five_D.ndim)