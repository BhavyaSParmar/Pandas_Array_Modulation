#!/usr/bin/env python
# coding: utf-8

# In[1]:


#HW1 - Bhavya Parmar


# In[2]:


# Q1. Creating Numpy Arrays:


# In[34]:


#1). Convert a Python list x=[[1,2,3],[4,5,6]] into a Numpy array. 
import numpy as np
x=[[1,2,3],[4,5,6]]

np_array=np.array(x)

print(np_array)


# In[31]:


#2). Use one line to create a 3x2 2D array with shape of (3,2), filled with 1-6.
import numpy as np

np.arange(1,7). reshape(3,2)


# In[35]:


#3). Use one line to create an array of 2, 4, 6, 8, ..., 98, 100; and find the mean value.  
import numpy as np

np.mean(np.arange(2,101,2))


# In[57]:


#4). Create an 3x3x3 array filled with arbitrary float numbers; and find the minimum and maximum values.
import numpy as np

x = np.random.random((3,3,3))

minimum_value = np.max(x)

maximum_value = np.min(x)

print('3x3x3 Array Is:')

print()

print(x)

print()

print('Maximum value is:', np.max(x))

print()

print('Minimum value is:', np.min(x))


# In[60]:


#5). Create a 3x4 2D array filled with values from 10 to 21 (included).
import numpy as np

x = np.arange(10,22).reshape(3,4)

print(x)


# In[62]:


#6). Create a numpy array of length 10, starting from 5 and has a step of 3 between consecutive numbers.
import numpy as np

x = np.arange(5,35,3)

print(x)


# In[69]:


#7). Create a shape (10,10) array with arbitrary values; and find the memory size of this array.
import numpy as np

x = np.random.random((10,10))

memorysize = x.nbytes

print(x)

print('The memory size of this array is:',memorysize)


# In[75]:


#8). Create a 1-d array of size 10 with arbitrary values but the fifth value should be 5.
import numpy as np

x = np.arange(1,11)

x[4]=5

print(x)


# In[86]:


#9). Create an array with values ranging from 10 to 49 (included); and reverse it then (first element becomes last).
import numpy as np

x = np.arange(10,50)

reverse_x = x[::-1]

print(reverse_x)


# In[123]:


#10). Create an array of shape (3, 2) with random values from a uniform distribution over [0, 1) and confirm you can get the same value when you run it next time.
import numpy as np

np.random.seed(10)

x = np.random.random((3,2))

print(x)


# In[146]:


#11). Create a 5x5 matrix with row values ranging from 0 to 4:  
import numpy as np

x = np.tile(np.arange(5.0), (5,1))

print(x)


# In[156]:


#12). Add a border (filled with 0's) around an existing array:
import numpy as np

#og = original array, fa = final array

import numpy as np

og = np.ones((5,5), dtype=int)

newshape = (og.shape[0] + 2, og.shape[1] + 2)

fa = np.zeros(newshape, dtype = int)

fa[1:-1, 1:-1, ] = og

print("The Original Array is:\n")

print(og,"\n")

print("------------------------\n")

print("The Final Array is\n")

print(fa)


# In[171]:


#13). Create a 5x5 2-d array with values 1,2,3,4,5 on the diagonal (3 points)  
import numpy as np

x = np.zeros((5,5), dtype = int)

np.fill_diagonal(x,[1,2,3,4,5])

print('The Array Is:\n',x)

y = np.zeros_like(x)

for i in range (1,5):
    for j in range(i):
        y[i,j] = x[i-1,j]
        
print('\n The New Desired Array Is\n', y)


# In[183]:


#14). Create a 10x10 2-d array with 1 (2 point) on the border and 0 inside
import numpy as np

x = np.zeros((10,10), dtype = int)

x[0,:] = 1 
x[-1,:] = 1 
x[:, 0] = 1
x[:, -1] = 1

print('The Array Is:\n', x)


# In[190]:


#Q15) Extract the integer part of a random array of positive numbers using 2 different methods, and the result should be an integer array.
import numpy as np

x = np.random.random((4,4)) * 100

y = x.astype(int)

print("Method 1 Result:")
print(y)

#Method 2

y2 = np.floor(x)

print("\nMethod 2 Result:")
print(y2)


# In[193]:


#Q2. Operations on Numpy Arrays
#1). Find the index of 5th repetition of number 1 in the given array x. 
import numpy as np

x = np.array([1,2,1,1,3,4,3,1,1,2,1,1,2])

case = np.where(x == 1)[0]

#index of the 5th repeating of number 1 in given array term as i5r

if len(case) >= 5:
    y = case[4]
    print("The Index of 5th repetation of integer 1 is :", y)
else:
    print("na")
    
    


# In[194]:


#Q2 Use np.arange to get an array [1, 2, 3, ..., 9]. Split x into 3 sub-arrays, the length of each sub-array is 4, 2, and 3.

import numpy as np

x = np.arange(1,10)

sub1 = x[:4]
sub2 = x[4:6]
sub3 = x[6:]

print(sub1)
print(sub2)
print(sub3)


# In[200]:


#Q3 Use np.arange to generate the following 2D array
#r = rows, c= column
#x = 1darray, y = 2darray
import numpy as np

r,c = 4,4

x = np.arange(0.0,16.0)

y = x.reshape(r,c)

print("2d Array Is:\n", y)

#part 2 Use np.split to split the array into left and right halves.

l , r = np.split(y,2,axis =1)

print("\nThe Left Array Is:")

print(l)

print("\nThe Right Array Is:")

print(r)


# In[205]:


#Q4 Given an 2D array:                                                 
#[[5,10,15],[20,25,30],[35,40,45]]

#(1) Slicing to get the sub-array [[10,15], [25,30]]

import numpy as np

x = np.array([[5,10,15],[20,25,30],[35,40,45]])

y = x[0:2,1:3]

print("The Subarray is \n ",y)

#(2) Getting individual element value "20"

print()

y2 = x[1,0]

print("Getting individual element value: \n", y2)


# In[207]:


#Q5  Let x be an array:  [[ 1 2 3], [ 4 5 6]] and y be an array [[ 7 8 9],[10 11 12]]. Concatenate x and y 
import numpy as np

x= np.array([[1,2,3], [4,5,6]])

y= np.array([[7,8,9],[10,11,12]])

answer = np.concatenate((x,y), axis = 1)

print("The Resulting Array Is:\n", answer)


# In[210]:


#Q6  Compute the min/max (min is divided by max) for each row for a given 2d array, in which integer values range from 1 to 10 [1,10) and shape is (5,3).

#Here requires a random seed to keep the same value from the random generator. 

import numpy as np

np.random.seed(10) #random seed 

x = np.random.randint(1,10, size = (5,3))

minvalue = np.min(x, axis = 1)
maxvalue = np.max(x, axis = 1)

ratio_min_max = minvalue / maxvalue

print("The array Is:")

print(x)

print("\nThe minimum value is ")

print(minvalue)

print("\nThe maximum value is ")

print(maxvalue)

print("\nThe min max ratio is ")

print(ratio_min_max)


# In[234]:


#Q7 Normalize a 5x5 random matrix:                          

#A normalization operates like: (the array - the mean)/the standard deviation

import numpy as np

m = np.random.rand(5,5)

meanvalue = np.mean(m)
std = np.std(m)

normalization = (m - meanvalue) / std

print("The Matrix Is:")

print(m)

print("\nThe Normalized matrix Is:")

print(Normalization)


# In[217]:


#Q8  Convert 3 arrays into a 1d array.                          

import numpy as np

x1 = np.arange(3)
x2 = np.arange(3,7)
x3 = np.arange(7,10)

y = np.concatenate((x1,x2,x3))

print("The Final One Dimensional Array Is:")

print(y)


# In[222]:


#Q9  Get all items between 15 and 55 from aa, math expression: [15,55]. The aa is uniformly distributed integers in a 1D array (size=20) with given values (<100). Requires defining a seed.

import numpy as np

np.random.seed(280)

size = 20

x = np.random.randint(0,100,size)

y = x[(x>=15) & (x<=55)]

print(y)


# In[225]:


#Q10  Get the positions where elements of a and b match. 

import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

matching = np.where(a == b)[0].tolist()

print("The Position where elements of A and B are matching in an array is:")
print(matching)


# In[229]:


#Q11 Use arange() to create an array from 0 to 20 ( [0,20) ); replace all odd numbers with -1.

import numpy as np

y = np.arange(0,20)

x = (y % 2 != 0)

y[x] = -1

print(y)


# In[232]:


#Q12 Considering a four dimensions array (3,4,3,4) with the values 0-9 randomly, how to get sum over the last two axis at once? 

import numpy as np

x = np.random.randint(0,10, size = (3,4,3,4))

y = np.sum(x, axis =(2,3))

print("The Resulting Array Is:")

print(x)

print("\nSum over the last two axis at once is:")

print(y)


# In[ ]:




