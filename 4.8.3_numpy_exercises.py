#!/usr/bin/env python
# coding: utf-8

# For even more practice, clone https://github.com/rougier/numpy-100, make your own repo called
# 
# numpy-100, and then commit and push your solutions to your own repo.

# In[1]:


import numpy as np


# ### a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# In[2]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[3]:


negatives = a < 0
positives = a > 0
evens = a % 2 == 0


# ### 1. How many negative numbers are there?

# In[4]:


negs = negatives.sum()


# ### 2. How many positive numbers are there?

# In[5]:


pos = positives.sum()


# ### 3. How many even positive numbers are there?

# In[6]:


posandeven = (a > 0) & (a % 2 == 0)
posandeven.sum()


# ### 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[7]:


new_a = a + 3
positives_new = new_a > 0
print(positives_new)
positives_new.sum()


# ### 5. If you squared each number, what would the new mean and standard deviation be?

# In[8]:


a_sqrd = a**2
new_mean = a_sqrd.mean()
new_std_dev = a_sqrd.std()
print("New mean", new_mean)
print("New std dev", new_std_dev)


# ### 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[9]:


mean = a.mean()
stda = a.std()
a_centered = a - mean
a_centered


# ### 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# $$Z = \frac{x − μ}{σ}$$

# In[10]:


z = a_centered / stda
print(z)


# In[11]:


points_and_zscores = list(zip(a_centered, z))
print(points_and_zscores)


# # Life w/o numpy to life with numpy

# In[12]:


## Setup 1
# Use python's built in functionality/operators to determine the following:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[13]:


a = np.array(a)


# #### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the # numbers in above list

# In[14]:


sum_of_a = a.sum()
sum_of_a


# ### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the #
# ### numbers in the above list

# In[15]:


min_of_a = a.min()


# #### Exercise 3 - Make a variable named max_of_a to hold the max number of all the 
# #### numbers in the above list

# In[16]:


max_of_a = a.max()


# #### Exercise 4 - Make a variable named mean_of_a to hold the average of all the #
# #### numbers in the above list

# In[17]:


mean_of_a = a.mean()


# #### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying 
# #### all the numbers in the above list together

# In[18]:


product_of_a = a.prod()
product_of_a


# #### Exercise 6 - Make a variable named squares_of_a. It should hold each number 
# #### in a squared like [1, 4, 9, 16, 25...]

# In[19]:


squares_of_a = a * a
squares_of_a


# #### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# In[20]:


odds_in_a = a % 2 == 1
odds_in_a


# #### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[21]:


evens_in_a = a % 2 == 0
evens_in_a


# ## Setup 2: 
# #### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, # a chessboard...

# In[22]:


# Consider what it would take to find the sum, min, max, average, sum, 
# product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]


# In[23]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
sum_of_b = b.sum()
sum_of_b


# In[24]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()
min_of_b


# In[25]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()


# In[26]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()


# In[27]:


# Exercise 5 - refactor the following to use numpy for calculating the product of 
# all numbers multiplied together.
product_of_b = b.prod()
product_of_b


# In[28]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b**2
squares_of_b


# In[29]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b % 2 == 1
odds_in_b


# In[30]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b % 2 == 0


# In[31]:


# Exercise 9 - print out the shape of the array b.
np.shape(b)


# In[32]:


# Exercise 10 - transpose the array b.
np.transpose(b)


# In[33]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.flatten()


# In[34]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing 
# only 1 number (6 x 1)


# In[35]:


b.reshape(6, 1)


# ## Setup 3
# #### HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

# In[36]:


c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# #### Exercise 1 - Find the min, max, sum, and product of c.

# In[37]:


c = np.array(c)


# In[38]:


c.min()


# In[39]:


c.max()


# In[40]:


c.sum()


# In[41]:


c.prod()


# #### Exercise 2 - Determine the standard deviation of c.

# In[42]:


c.std()


# #### Exercise 3 - Determine the variance of c.

# In[43]:


print(c.var())


# #### Exercise 4 - Print out the shape of the array c

# In[44]:


print(np.shape(c))


# #### Exercise 5 - Transpose c and print out transposed result.

# In[45]:


print(np.transpose(c))


# #### Exercise 6 - Get the dot product of the array c with c. 

# In[46]:


np.dot(c, c)


# #### Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# In[47]:


sum_c_trans_c = (c * np.transpose(c)).sum()
print(sum_c_trans_c)


# #### Exercise 8 - Write the code necessary to determine the product of c times c  transposed. Answer should be 131681894400.

# In[48]:


product_c_trans_c = (c * np.transpose(c)).prod()
print(product_c_trans_c)


# ## Setup 4

# In[49]:


d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# #### Exercise 1 - Find the sine of all the numbers in d

# In[50]:


d = np.array(d)
print(np.sin(d))


# #### Exercise 2 - Find the cosine of all the numbers in d

# In[63]:


print(np.cos(d))


# #### Exercise 3 - Find the tangent of all the numbers in d

# In[52]:


print(np.tan(d))


# #### Exercise 4 - Find all the negative numbers in d

# In[68]:


print(d < 0)


# #### Exercise 5 - Find all the positive numbers in d

# In[69]:


print(d > 0)


# #### Exercise 6 - Return an array of only the unique numbers in d.

# In[55]:


unique_numbers = np.unique(d)
print(unique_numbers)


# #### Exercise 7 - Determine how many unique numbers there are in d.

# In[57]:


unique_numbers.size


# #### Exercise 8 - Print out the shape of d.

# In[58]:


d.shape


# #### Exercise 9 - Transpose and then print out the shape of d.

# In[59]:


d.transpose()


# #### Exercise 10 - Reshape d into an array of 9 x 2

# In[60]:


d.reshape(9, 2)

