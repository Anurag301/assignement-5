#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Parent and child class
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,InterestRate=0):
        super().__init__(title, balance)
        self.title=title
        self.balance=balance
        self.InterestRate=InterestRate
A=Account("rishi", 100)
SA=SavingsAccount("rishi", 100, 1)
print(f"Here, {SA.title} is the title, {SA.balance} is the balance and {SA.InterestRate} is the interestRate.")


# In[ ]:




