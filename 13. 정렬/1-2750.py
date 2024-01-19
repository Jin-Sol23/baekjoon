# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:01:08 2024

@author: adam
"""

# 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

'''
입력 : 
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
수는 중복되지 않는다.
'''

# 출력 : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력1
5
5
2
3
4
1

# 예제 출력1
1
2
3
4
5

#%%
'''
1. n을 입력받는다.
2. n을 for문으로 돌림
for i in range(n):
3. 정수 a를 n번 입력받음
4. 입력받은 a를 alist=[]에 append를 사용하여 추가함
alist = [a1, a2, a3, a4, a5]
5. for문을 사용하여 alist를 돌리고,
if문을 사용하여 값을 비교함
'''
#%%
n = int(input())

alist = []
for _ in range(n):
    a = int(input())
    alist.append(a)
    alist.sort()

for i in range(len(alist)):
    print(alist[i])

#%%
# (검색) sort 사용안하고 푸는법
n = 5

for _ in range(n):
    alist = [5, 2, 3, 4, 1]

for i in range(len(alist)):
    k = len(alist) - i # k = 5 / 4 / 3 / 2 / 1
    for j in range(1, k): # j = 1 / 2 / 3 / 4 / 1 / 2 / 3 / 1 / 2 / 1
        if alist[j-1] >= alist[j]: # 5 >= 2 (True)
            temp = alist[j-1] # temp 변수에 5를 넣음
            alist[j-1] = alist[j] # 5(alist[0]) 대신 2를 넣음
            alist[j] = temp # 2 (alist[j]) 대신에 5를 넣음
            
            
print(alist)
    
#%%
'''
1. alist[0]에 있는 5를 alist[0:4]까지 차례대로 크기를 비교함,
5보다 크기가 작으면 
'''

#%%

n = 5
alist = [5, 2, 3, 4, 1]

# alist[0]에 있는 5를 alist[0:4]까지 차례대로 크기를 비교함
for i in range(len(alist)):
    if alist[0] > alist[1]: # alist[0] > alist[1] 이면, 둘의 순서를 변경하려함
        temp = alist[0] # 변경하려면 temp 변수를 만들어서 alist[0]을 임시로 넣어두고,
        alist[0] = alist[1] # alist[1]을 alist[0]에 넣은 후, temp에 있는 alist[0]을 alist[1]로 넣음 
        alist[1] = temp # alist = [2, 5, 3, 4, 1]
        
for i in range(len(alist)):
    if alist[1] > alist[2]:
        temp = alist[1]
        alist[1] = alist[2]
        alist[2] = temp # alist = [2, 3, 5, 4, 1]

for i in range(len(alist)):
    if alist[2] > alist[3]:
        temp = alist[2]
        alist[2] = alist[3]
        alist[3] = temp # alist = [2, 3, 5, 4, 1]

for i in range(len(alist)):
    if alist[3] > alist[4]:
        temp = alist[3]
        alist[3] = alist[4]
        alist[4] = temp # alist = [2, 3, 4, 1, 5], alist[0:4]까지 차례대로 끝까지 비교 완료

for i in range(len(alist)):
    if alist[0] > alist[1]:
        temp = alist[0]
        alist[0] = alist[1]
        alist[1] = temp # alist = [2, 3, 4, 1, 5]     
        print(alist)

for i in range(len(alist)):
    if alist[1] > alist[2]:
        temp = alist[1]
        alist[1] = alist[2]
        alist[2] = temp # alist = [2, 3, 4, 1, 5]
        print(alist)

for i in range(len(alist)):
    if alist[2] > alist[3]:
        temp = alist[2]
        alist[2] = alist[3]
        alist[3] = temp # alist = [2, 3, 1, 4, 5]
        print(alist)

for i in range(len(alist)):
    if alist[3] > alist[4]:
        temp = alist[3]
        alist[3] = alist[4]
        alist[4] = temp # alist = [2, 3, 1, 4, 5], alist[0:4]까지 차례대로 끝까지 비교 완료
        print(alist)

for i in range(len(alist)):
    if alist[0] > alist[1]:
        temp = alist[0]
        alist[0] = alist[1]
        alist[1] = temp # alist = [2, 3, 4, 1, 5]     
        print(alist)

for i in range(len(alist)):
    if alist[1] > alist[2]:
        temp = alist[1]
        alist[1] = alist[2]
        alist[2] = temp # alist = [2, 1, 3, 4, 5]
        print(alist)

for i in range(len(alist)):
    if alist[2] > alist[3]:
        temp = alist[2]
        alist[2] = alist[3]
        alist[3] = temp # alist = [2, 1, 3, 4, 5]
        print(alist)

for i in range(len(alist)):
    if alist[3] > alist[4]:
        temp = alist[3]
        alist[3] = alist[4]
        alist[4] = temp # alist = [2, 1, 3, 4, 5], alist[0:4]까지 차례대로 끝까지 비교 완료
        print(alist)

for i in range(len(alist)):
    if alist[0] > alist[1]:
        temp = alist[0]
        alist[0] = alist[1]
        alist[1] = temp # alist = [1, 2, 3, 4, 5]    
        print(alist)

for i in range(len(alist)):
    if alist[1] > alist[2]:
        temp = alist[1]
        alist[1] = alist[2]
        alist[2] = temp # alist = [2, 1, 3, 4, 5]
        print(alist)

for i in range(len(alist)):
    if alist[2] > alist[3]:
        temp = alist[2]
        alist[2] = alist[3]
        alist[3] = temp # alist = [2, 1, 3, 4, 5]
        print(alist)

for i in range(len(alist)):
    if alist[3] > alist[4]:
        temp = alist[3]
        alist[3] = alist[4]
        alist[4] = temp # alist = [2, 1, 3, 4, 5], alist[0:4]까지 차례대로 끝까지 비교 완료
        print(alist)

print(alist)


#%%
# 위의 노가다를 해보고 알게됨 : 아래 코드를 n-1번 반복하면 정렬됨, 예외는 없음
n= 5
alist = [5, 2, 3, 4, 1]

for j in range(n-1):
    for i in range(len(alist)):
        if alist[0] > alist[1]:
            temp = alist[0]
            alist[0] = alist[1]
            alist[1] = temp  
            print(alist) # 다음줄에 띄어쓰기가 있어서 위의 for문(j index)으로 돌아갈 수도 있겠다고 생각했는데 2번째 for문(i index)로 넘어감, 들여쓰기를 해서 그런것 같음
    
    for i in range(len(alist)):
        if alist[1] > alist[2]:
            temp = alist[1]
            alist[1] = alist[2]
            alist[2] = temp
            print(alist)
    
    for i in range(len(alist)):
        if alist[2] > alist[3]:
            temp = alist[2]
            alist[2] = alist[3]
            alist[3] = temp 
            print(alist)
    
    for i in range(len(alist)):
        if alist[3] > alist[4]:
            temp = alist[3]
            alist[3] = alist[4]
            alist[4] = temp
            print(alist)

#%%        
# 위의 i index for문 4개가 규칙적임. i로 바꿔서 더 줄였음
# 오류남 (IndexError)
n= 5
alist = [5, 2, 3, 4, 1]

for j in range(n-1):
    for i in range(len(alist)): # i = 0 / 1 / 2 / 3 / 4
        if alist[i] > alist[i+1]: # IndexError: list index out of range (index가 범위 밖에 있다고함)
            temp = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = temp  
            print(alist)

# i = 4일때 i+1을하면 i가 alist[5]가 되서 오류남
        
#%%       
n= 5
alist = [5, 2, 3, 4, 1]

for j in range(n-1):
    for i in range(len(alist)): # i = 0 / 1 / 2 / 3 / 4
        if alist[i-1] > alist[i]: # 1 > 5 (False라서 if문에 안들어감)
            temp = alist[i-1]
            alist[i-1] = alist[i]
            alist[i] = temp  
print(alist)        

# alist[i-1] == alist[-1] == 1

for results in range(len(alist)):
    print(alist[results])
#%%
# 백준 제출 형식에 맞도록 수정해서 제출했는데 자꾸 틀렸다고 나옴;;
n = int(input())
     
alist = []
for _ in range(n):
    a = int(input())
    alist.append(a)

for j in range(n-1):
    for i in range(len(alist)):
        if i > 0: # i[-1] > i[0] 이 5 > 1 이라고 가정할때, 서로 자리가 바뀌게 됨. 그래서 i는 0보다 커야함 
            if alist[i-1] > alist[i]:
                temp = alist[i-1]
                alist[i-1] = alist[i]
                alist[i] = temp

for alist_idx in range(len(alist)):
    print(alist[alist_idx])


#%% 다른 사람 답변
N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

for i in range(len(M)):
    for j in range( len(M)): # 같은걸 이중 반복 하는구나
        if M[i]<M[j]:
            M[i],M[j] = M[j],M[i] # !!!
for k in M:
    print(k)

#%% temp 없이 자리 바꾸기
a = [1, 2, 3, 4]
a[0], a[2] = a[2], a[0]
print(a) # [3, 2, 1, 4]
