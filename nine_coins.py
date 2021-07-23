#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Nine_Coins Class


# In[2]:


import random


# In[4]:


class Nine_Coins:
    def __init__(self, num):
        self.num = num
        self.binary ="{:09b}".format(self.num) #將num轉換成二進制，不足9位數則補0
        self.state = str(self.binary)
        self.state = self.state.replace("0","H")  #0換成 H
        self.state = self.state.replace("1","T")  #1換成 T
                          
    def toss(self):  #產生隨機狀態
        self.num = random.randint(0, 511)
        self.binary ="{:09b}".format(self.num)
        self.state = str(self.binary)
        self.state = self.state.replace("0","H")
        self.state = self.state.replace("1","T")
        
    def __repr__(self):
        return f"Nine_Coins: {self.state}"
        
        
    def __str__(self):
        return f"binary: {self.binary} and decimal: {self.num}"
            
    


# In[ ]:




