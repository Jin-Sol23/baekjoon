# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:31:16 2023

@author: adam
"""

#%%
# 전에 풀었던 코드 (다 못풀었음)
a, b = map(int, input().split())
c = int(input())

if b + c >= 60:
    if (b + c) % 60 == 0:
        bc = (b + c) // 60
        print(a + bc, 0)
    else:
        bc = (b + c) // 60
        print(a + bc, b + c - bc)
else:
    print(a, b + c)

#%%
h = 17
m = 40
c = 80

print(h+((m+c)//60), (m+c)%60) # 숫자를 대입하여 식을 만들었음
#%%
h = 23
m = 48
c = 25

print(h+((m+c)//60), (m+c)%60)

#%%
# 문제 다시 풀었음 (풀이 완료, 저번보다 코드 길이 짧아짐)
h, m = map(int, input().split())
c = int(input())

if h+((m+c)//60) >= 24:
    print((h+(m+c)//60)%24, (m+c) % 60) # h 빼먹고, %24 안해서 계속 틀림
elif h+((m+c)//60) < 24:
    print(h+((m+c)//60), (m+c) % 60)

#%%
# chat GPT 답변
h, m = map(int, input().split())
c = int(input())

total_minutes = h * 60 + m + c
new_h = total_minutes // 60 % 24
new_m = total_minutes % 60

print(new_h, new_m)