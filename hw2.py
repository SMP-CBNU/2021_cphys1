#!/usr/bin/env python
# coding: utf-8

# ## 함수를 이용하여 다음의 조건에서 $n=1$에서 $20$까지 로지스틱 맵의 값을 구하여라. 

# $$ f_{n+1} = rf_n(1-f_n) $$

# In[1]:


n=0
f_n=0.5
r=4.5


# In[2]:


while n < 20 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# In[3]:


n=0
f_n=0.51
r=4.5


# In[4]:


while n < 20 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# In[5]:


n=0
f_n=0.501
r=4.5


# In[6]:


while n < 20 :
    n += 1
    f_n = r*f_n*(1-f_n) 
    print(n, f_n)


# $$ f_1 = f_2 = 1, $$
# $$ f_n=f_{n-1}+f_{n-2}$$

# In[7]:


# n은 양의 정수
def fibonacci(n): 
    if n <= 2: 
        return(1)
    elif n >= 3:
        return(fibonacci(n-1)+fibonacci(n-2))
for i in range(1,13):
    print(i,fibonacci(i))


# In[8]:


fibonacci(10)


# In[9]:


fibonacci(11)


# In[10]:


fibonacci(12)


# # n번째 피보나치를 구하는 함수는 fibonacci(n) 이다.
