# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:44:15 2024

@author: adam
"""

#%%
# 1-7-10926
site = input()
print(site + "??!")

#%%
# 1-11-11382
a, b, c = map(int, input().split())
print(a+b+c)

#%%
# 2-2-9498
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")
    
#%%
# 3-1-2739
# 구구단
n = int(input())
for i in range(1, 10):
    print("{0} * {1} = {2}" .format(n, i, n*i))

#%%
# 3-2-10950
t = int(input())
for i in range(0, t):
    a, b = map(int, input().split())
    print(a+b)

#%%
# 3-3-8393
n = int(input())
a = 0
for i in range(1, n+1):
    a += i
print(a)

#%%
# 3-4-25304
total = int(input())
n = int(input())
c = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    c += (a * b)
if total == c:
    print("Yes")
else:
    print("No")
    
#%%
# 3-7-11021
t = int(input())
for i in range(1, n+2):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a+b)

#%%
# 3-8-11022
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a, "+", b, "=", a+b)

#%%
# 3-9-2438
n = int(input())
for i in range(1, n+1):
    print(i*"*")
    
#%%
# 3-11-10952
a = 1
b = 1
while a != 0 and b != 0:
    a, b = map(int, input().split())
    if a+b == 0:
        break
    print(a+b)

#%%
# 3-12-10951
try: # 에러가 발생할 것으로 예상되는 곳에 작성
    while True:
        a, b = map(int, input().split())
        print(a+b)
# try 내부에서 에러가 발생하면 바로 except 구문으로 넘어감
except: # 에러를 처리할 코드 작성
    pass