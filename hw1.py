#!/usr/bin/env python
# coding: utf-8

# In[1]:


r = 0.5
n = 0
f_n = 0.5

while n < 10 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# In[2]:


r = 2.5
n = 0
f_n = 0.5

while n < 10 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# In[3]:


r = 4.5
n = 0
f_n = 0.5

while n < 10 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# In[4]:


r = 4.5
n = 0
f_n = 0.51

while n < 10 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)

