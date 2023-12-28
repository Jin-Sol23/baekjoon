# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:44:04 2023

@author: adam
"""

s = input().split()
print(s) # ['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button']

#%%
str = input().split()
a = []
for i in range(len(str)):
    a.append(i)
print(i + 1) # NameError : for 루프 안에 있는 i를 for 루프 종료된 후에도 사용하려고 해서 오류남

# GPT 답변
# i 대신 다른 변수를 사용하거나 i를 루프 외부에서 사용하는 방법이 있음

#%%
str = input().split()
a = []
for i in range(len(str)):
    a.append(i)
    
# 여기서부터는 루프 외부입니다.
print(i + 1) # GPT가 알려준대로 했는데 같은 오류남

#%%
a = []
while True:
    s = input().split()
    for i in range(len(s)):
        a.append(i)
        ii = i
    print(ii+1)
    break

#%% 아....
s = input().split()
print(len(s))