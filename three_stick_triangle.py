#!/usr/bin/env python
# coding: utf-8

# problem T.P - 3

# In[2]:


def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("Yes")
    else:
        print("No")


# In[23]:


def promp_user():
    
        a = int(input("Enter the length of the first stick: "))
        b = int(input("Enter the length of the second stick: "))
        c = int(input("Enter the length of the third stick: "))
        
        is_triangle(a, b, c)
           
    


# In[25]:


promp_user();


# In[ ]:




