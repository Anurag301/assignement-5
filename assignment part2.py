#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Calculator
class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def substract(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num2/self.num1
c=Calculator(10,94)
print(c.add())
print(c.substract())
print(c.multiply())
print(c.divide())


# In[ ]:




