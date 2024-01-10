# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:42:07 2024

@author: adam
"""

'''
문제 : 
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다.
이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다.
따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
'''

# 입력 : 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 출력 : 첫째 줄에 상수의 대답을 출력한다.


#%%
'''
input().split() 734, 893
range(::-1) i = 4 3 7
range(::-1) j = 3 9 8
if 문으로 비교
'''

#%%
a, b = input().split()
a = list(str(a))
b = list(str(b))

aa = []
bb = []
for i in a[::-1]:
    aa.append(i)
for j in b[::-1]:
    bb.append(j)
        
if aa > bb:
    for a_i in aa:
        print(a_i, end='')
elif aa < bb:
    for b_i in bb:
        print(b_i, end='')

#%% 다른 사람 코드1
a,b = input().split()
a = a[::-1]
b = b[::-1]
print(max(int(a),int(b)))

#%% 다른 사람 코드2
a,b = input().split()

A = a[-1::-1]
B = b[-1::-1]

if int(A)>int(B):
    print(A)
else:
    print(B)