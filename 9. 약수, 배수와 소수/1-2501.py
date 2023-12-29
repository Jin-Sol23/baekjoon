# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:43:54 2023

@author: adam
"""

# 약수 구하기

# 문제 : 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

# 출력 : 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다.
# 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

#%%
# 망함
a = 6
k = 4
c = []
for i in range(1, a+1):
    if a % i == 0:
        c.append(i)
    
if k > len(c):
    print(0)
else:
    print(c[k-1])

#%%
# 망함
n, k = map(int, input().split())

if n % k == 0:
    for i in range(1, n+1):
        if k == i:
            a = i
    print(i)
else:
    print(0)

#%%
# 출력이 잘 되서 약수가 없을 때 0 출력을 아래 코드에 추가함
n, k = map(int, input().split())
c = []

for i in range(1, k+1):
    if n % i == 0:
        c.append(i)
print(c.index(k)+1)

#%%
# 0 출력하도록 if, else문 추가하니까 망함
n, k = map(int, input().split())

c = []
if n % i != 0:
    print(0)
else:
    for i in range(1, k+1):
        if n % i == 0:
            c.append(i)
    print(c.index(k)+1)

#%%
# 위의 코드를 chat GPT에게 수정할 부분 어디냐고 문의함 (채점 결과 : 실패)
n, k = map(int, input().split())

c = []
if n % k != 0:
    print(0)
else:
    for i in range(1, n + 1):
        if n % i == 0:
            c.append(i)
    if k not in c:
        print(0)
    else:
        print(c.index(k) + 1)


#%%
# chat GPT 답변 수정+수정 (채점 결과 : 또 틀림)

n, k = map(int, input().split())
    
c = []
for i in range(1, k+1):
    if n % i == 0:
        c.append(i)
    
c.sort()
    
if k not in c:
    print(0)
else:
    print(c.index(k)+1)

#%%
# 블로그 풀이
n, k = map(int, input().split())

c = []
for i in range(1, n+1):
    if n % i == 0:
        c.append(i)
     
if k > len(c):
    print(0)
else:
    print(c[k-1])