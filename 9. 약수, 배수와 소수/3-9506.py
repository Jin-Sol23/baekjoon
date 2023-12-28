# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:27:21 2023

@author: adam
"""
a = []
while True:
    n = input()
    n = int(n)
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                a.append(i)
                if sum(a) == n:
                    print(a)
#                else:
#                    print("{0} is NOT perfect." .format(n))
            

#%%
n = 28
a = []
for i in range(1, n):
    if n % i == 0:
        a.append(i)
        if sum(a) == 0:
            #print(i)
            print(a)
       # if sum(a) == n:
           # print()
            #print("{0} = ","{1} +" .format(n, i[0]))

#%%
a = []
b = []
while True:
    n = input()
    n = int(n)
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                a.append(i)
                
    if sum(a) == n:
        print(a)
    else:
        print("{0} is NOT perfect." .format(n))
    