#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lambda arguments:expression
x=lambda a:a +10
print(x(5))


# In[2]:


x=lambda a,b : a*b
print(x(5, 6))


# In[3]:


x=lambda a, b, c :a +b +c
print(x(4,5,6))


# In[7]:


def my_function(n):
    return lambda a:a*n
mydoubler=my_function(2)
mytripler=my_function(3)

print(mydoubler(11))

print(mytripler(11))


# In[ ]:




