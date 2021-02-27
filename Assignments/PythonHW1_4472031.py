#!/usr/bin/env python
# coding: utf-8

# # Python Homework 1
# 
# **Release date:** Friday, January 10th <br>
# **Due date:** Friday, January 24th, 11:59 p.m. via GauchoSpace
# 
# **Instruction:** Please upload your pdf or html file with your code and result on GauchoSpace with filename "PythonHW1_YOURPERMNUMBER".
# 

# The purpose of this Python Homework is to get a little bit familiar with sampling from a distribution with the __NumPy Package__.
# 
# _Attention:_ Don't forget to import the necessary packages!

# ## Problem 1 (6 Points)

# 1. Simulate 100,000 realizations from the binomial distribution with $N$=1000 trails and success probability $p$=0.3.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import time


# In[3]:


#100,000 simulated realizations
a = np.random.binomial(n=1000, p=0.3, size = 100000)


# 2. Compute the empirical mean and the empricial standard deviation of your sample and compare these values with the theoretical values.

# In[4]:


#empirical mean
emp_mean = np.mean(a)
emp_mean
#theoritical value is 300


# In[5]:


#empirical standard deviation
emp_std = np.std(a)
emp_std
#theorital value is 14.49


# 3. Plot a histogram of your sample with the absolute number of counts for each bin. Choose 25 bins.

# In[8]:


plt.hist(a, bins = 25, density = False)
plt.xlabel('Probability of success')
plt.ylabel('Number of trials')
plt.title('Histogram')
plt.grid(True)
plt.show()


# 4. Standardize your sample, that is, subtract the emprical mean and divide by the empricial standard deviation.

# In[14]:


(300-emp_mean)/emp_std


# 5. Plot a histogram of your standardized sample with the counts normalized to form a probability density. Choose again 25 bins. Compare your histrogram with the density of the standard normal distribution by inserting its density into the histogram plot. 

# In[10]:


b = []
for i in range(0,len(a)):
    b.append((a[i] - emp_mean)/emp_std)
m, bins, patches = plt.hist(b, 25,facecolor='g', alpha=0.5,density = True,label='standardized sample')
stnm = np.random.standard_normal(100000)
m, bins, patches = plt.hist(stnm, 25,facecolor='r', alpha=0.5,density = True,label='standard normal dist')
plt.legend()
plt.xlabel('Standard Deviation')
plt.ylabel('Normalized counts')
plt.title('Histogram')
plt.grid(True)
plt.show()


# ## Problem 2 (4 Points)

# 1. Implement the simulation of a biased 6-sided die which takes the values 1,2,3,4,5,6 with probabilities 1/8,1/12,1/8,1/12,1/12,1/2.

# In[26]:


p = [1/8, 1/12, 1/8, 1/12, 1/12, 1/2]
die = [1,2,3,4,5,6]


# 2. Plot a histrogramm with 1,000,000 simulations to check if the relative counts of each number is approximately equal to the corresponding specified probabilities.
# 
# _Remark:_ Specify the bins of your histogram correctly.

# In[43]:


import numpy as np


# In[44]:


rolls = list(np.random.choice(die, 1000000, p=p))
sample = np.random.choice(die, [1000000], p)


# In[45]:


counts = [rolls.count(i) for i in die]
probs = [float(counts[i])/1000000 for i in range(6)]
print(probs)


# In[46]:


plt.hist(rolls)
plt.title('Histogram')


# In[ ]:




