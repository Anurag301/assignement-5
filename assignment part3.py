#!/usr/bin/env python
# coding: utf-8

# In[9]:



# Complete Student Class
class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollno):
        self.__rollno=rollno
    def getRollNumber(self):
        return self.__rollno
s=Student()
s.setName("anurag")
print(s.getName())
s.setRollNumber(5)
print(s.getRollNumber())


# In[ ]:




