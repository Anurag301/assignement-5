#!/usr/bin/env python
# coding: utf-8

# In[13]:


def withdrawal(self, amount):
        self.balance=self.balance - amount
        return self.balance


    def deposit(self, amount):
       self.balance=self.balance + amount 
       return self.balance

    def getBalance(self):
        return self.balance


# In[ ]:




