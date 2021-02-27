#!/usr/bin/env python
# coding: utf-8

# # Python Homework 3
# 
# **Release date:** Monday, January 27th <br>
# **Due date:** Friday, __Feb 7th__, 11:59 p.m. via GauchoSpace
# 
# **Instruction:** Please upload your pdf or html file on GauchoSpace with filename "PythonHW3_YOURPERMNUMBER.ipynb".
# 

# In this Python Homework you are asked to implement two simulations related to problems discussed in class.
# 

# As usual, start with loading some packages:

# In[14]:


import numpy as np
from enum import Enum
from random import randint


# ## Problem 1 (5 Points)
# 
# Since the beginning of Spring quarter Julie goes every day to Woodstock Pizza, orders a slice of pizza, and picks a topping - pepper, pepperoni, pineapple, prawns, or prosciutto - unifromly at random. 

# 1. Implement a simulator which uniformly samples from one topping:

# In[18]:


# number the toppings
class topping(Enum):
    pepper = 1
    pepperoni = 2
    pineapple = 3
    prawns = 4
    prosciutto = 5

# randomly generate a topping
def simulation():
    num = randint(1, 5)
    return topping(num)


# 2. On the day that Julie first picks pineapple, find the empricial mean of the number of prior days in which she picked pepperoni by running 10000 simulations.
# 
# 

# In[16]:


# simulation mean of pepporoni before pineapple 
def pepperoni_before_pineapple():
    number = 0
    for i in range(10000):
        Top = simulation()
        while Top != topping.pineapple:
            if Top == topping.pepperoni:
                number = number + 1
            Top = simulation()
            mean = number / 10000
    return mean

print(pepperoni_before_pineapple())


# ## Problem 2 (5 Points)
# 
# Recall Problem 3.3:
# 
# A health insurance will pay for a medical expense subject to a USD 100 deductible. Assume that the amount of the expense is exponentially distributed with mean USD 500.
# 
# Compute the empirical mean and emprical standard deviation of the payout by the insurance company by using 100000 samples.

# In[20]:


# Sample from exponential distribution
expense_amount = np.random.exponential(size = 100000, scale = 500)

# Empirical mean and std
for i in range(len(expense_amount)):
    expense_amount[i] -= 100
mean = np.mean(expense_amount)
standard_deviation = np.std(expense_amount)
print(mean, standard_deviation)


# In[ ]:




