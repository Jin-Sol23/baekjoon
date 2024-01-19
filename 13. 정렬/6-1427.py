# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:54:10 2024

@author: adam
"""

# 입력 : 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 출력 : 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# 예제 입력 1 : 2143
# 예제 출력 1 : 4321

# 예제 입력 2 : 500613009
# 예제 출력 2 : 965310000


#%%
n = 2143
nstr = str(n) # nstr = <class 'str'>
# print(type(nstr))

nstr_list = []
for nstr_idx in range(len(nstr)): # nstr = '2143'
    nstr_list.append(int(nstr[nstr_idx])) # nstr_list = [2, 1, 4, 3]
#    print(nstr_list)

for i in range(len((nstr_list))):
    for j in range(len(nstr_list)):
        if nstr_list[i] > nstr_list[j]:
            nstr_list[i], nstr_list[j] = nstr_list[j], nstr_list[i]
#            print(nstr_list)

for results in range(len(nstr_list)):
    print(nstr_list[results], end='')

#%% 백준 제출
n = input()

nstr_list = []
for nstr_idx in range(len(n)):
    nstr_list.append(int(n[nstr_idx]))

for i in range(len((nstr_list))):
    for j in range(len(nstr_list)):
        if nstr_list[i] > nstr_list[j]:
            nstr_list[i], nstr_list[j] = nstr_list[j], nstr_list[i]

for results in range(len(nstr_list)):
    print(nstr_list[results], end='')