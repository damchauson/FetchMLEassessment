#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
import math
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_daily.csv')

dd = {}
numdays = {}
for i in range(data.shape[0]):
    _,m,_ = data['# Date'][i].split('-')
    dd[int(m)] = data['Receipt_Count'][i] + dd.get(int(m),0)
    numdays[int(m)] = 1 + numdays.get(int(m),0)
#print(dd)
#print(numdays)
"""datadict = {"Month":[], "NumDays":[], "Receipts":[]}
for key in dd:
    datadict["Month"].append(key)
    datadict["NumDays"].append(numdays[key])
    datadict["Receipts"].append(dd[key])
df = pd.DataFrame(datadict)"""

# w = (X.T @ X)^-1 @ X.T @ y
X = np.zeros((12,2))
y = np.zeros(12)
for i in range(12):
    X[i][0] = i+1
    X[i][1] = numdays[i+1]
    y[i] = dd[i+1]
w = np.linalg.inv(X.T @ X) @ X.T @ y

while(True):
    month = input("Enter month (number), or type 'exit' to quit: ")
    if month == "exit":
        break
    elif month in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        print(w[0]*int(month) + w[1]*numdays[int(month)])
    else:
        print("Invalid input; please try again")
