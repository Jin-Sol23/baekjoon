# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:48:45 2024

@author: iris
"""

'''
문제 :
도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
도현이는 앞으로 M번 공을 넣으려고 한다.
도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고,
정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
공을 넣을 바구니는 연속되어 있어야 한다.
공을 어떻게 넣을지가 주어졌을 때,
M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
'''

'''
입력 :
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
각 방법은 세 정수 i j k로 이루어져 있으며,
i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다.(1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
도현이는 입력으로 주어진 순서대로 공을 넣는다.
'''

# 출력 : 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
# 공이 들어있지 않은 바구니는 0을 출력한다.

'''
예제 입력1
5 4
1 2 3
3 4 4
1 4 1
2 2 2
'''

# 예제 출력1 : 1 2 1 1 0
#%%
# 문제에 대한 전체적인 그림을 그려서 png 이미지 파일로 저장해 놓았다.
from PIL import Image
from PIL import ImageDraw

img1 = Image.open('4-5-10810.png')
img1 # 그림이 console 창에 나타남, 사이즈도 너무 큼
 
#%%
# 그림을 plots 창에 나타내고 싶었음
# pip install opencv-python

import cv2
import matplotlib.pyplot as plt

ppt_image = plt.imread('4-5-10810.png', cv2.IMREAD_COLOR)

fig = plt.figure(num=1, figsize=(10,15))
plt.imshow(ppt_image)

#%%
'''
1. 1부터 n까지 바구니를 만든다.
바구니가 있어야 공을 넣을 수 있기 때문에 바구니를 먼저 만든다.
바구니는 리스트로 [1, 2, 3, 4, 5] 와 같이 만든다.
2. m번에 걸쳐 바구니에 공을 넣는 방법이 주어진다.
for문을 통해 i, j, k를 m번 반복하여 입력받는다.
3. m에서 입력받은(공을 넣어야하는) 바구니 시작(i)~끝(j)을 슬라이싱한다. 바구니[i:j]
슬라이싱을 해야되서 맨처음에 바구니를 리스트 형식으로 만들어야 한다.
4. 슬라이싱한 바구니[i:j]에 k번이 적힌 공을 대입하여 넣는다.
그냥 안들어가서 for문으로 넣는다.
5. 한 바구니에는 1개의 공만 넣을 수 있다고 했으니까
한 바구니에 공의 개수가 1개일 때 m번을 반복하여 1개를 더 추가하여 2개가 될거라면
pop으로 이미 들어있는 공 1개를 뺀 후에 다음 공을 추가한다. (바구니에 공은 계속 1개만)
6. 모든 바구니에 있는 공의 번호를 출력한다.


'''
#%%
n, m = map(int, input().split())
    
for ball in range(1, m+1):
    i, j, k = map(int, input().split())
    basket = []
    for a in range(1, n+1):
        basket.append(a) # basket = [1, 2, 3, 4, 5]
        ij_basket = []
    for z in basket[i-1:j]:
        ij_basket.append(k)
        basket.append(ij_basket)
print(basket)


#%%
'''
1. m은 공이 아니라 방법이다. 따라서 바구니와 공을 각각 만들어야 한다.
2. 바구니 n개, 공 n개를 반복문으로 만든다.
3.
'''
#%%
n, m = map(int, input().split())
# basket = []
#for a in range(1, n+1):
#    basket.append(a)
    
for mtd in range(1, m+1): # mtd = 1, 2, 3, 4
    i, j, k = map(int, input().split())
    basket = []
    for n_idx in range(1, n+1): # n_idx = 1, 2, 3, 4, 5
        basket.append(n_idx) # basket = [1, 2, 3, 4, 5]
        for mtd_ball in basket[i-1:j]:
            print(mtd_ball)
            ij_basket.append(k)
            basket.append(ij_basket)
    print(basket)

#%%
n, m = map(int, input().split())

basket = []
for n_idx in range(1, n+1): # n_idx = 1 / 2 / 3 / 4 / 5
    basket.append(n_idx*0) # basket = [0, 0, 0, 0, 0]
    
for mtd in range(1, m+1): # mtd = 1 / 2 / 3 / 4
    i, j, k = map(int, input().split())
    basket[i-1:j].pop()
    basket[i-1:j] = [k]
    print(basket)
#    mtd_basket = basket[i-1:j] # mtd_basket = [1, 2] / [3, 4] / [1, 2, 3, 4] / [2]
#    basket[mtd_basket] = k
#    print(basket)
#%%
'''
1. 1부터 n까지 바구니를 만든다.
바구니가 있어야 공을 넣을 수 있기 때문에 바구니를 먼저 만든다.
바구니의 번호는 상관이 없으므로 리스트로 [0, 0, 0, 0, 0] 과 같이 만든다.
2. m번에 걸쳐 바구니에 공을 넣는 방법이 주어진다.
for문을 통해 m번이 반복되는 것과 동시에 i, j, k도 같이 반복된다. _total에 저장한 숫자가 하나씩 대입된다.
3. i~j의 바구니에 k를 넣어야 한다. m, i, j 의 인덱스가 0일때, 1-2번 바구니에 3번 공을 각각 넣어야하니까
위의 2단계의 for문이 돌아갈때 k를 넣어야 한다. 그러므로 2단계 for문 밑에 i~j범위의 바구니에 k를 넣는다.
k의 type이 int이므로 슬라이싱해서 대입할 수 없다. (error : basket[i:j] = k)
for문을 추가하여 range(i, j)를 하고, ball에 index를 대입하고, basket[index]를 하여  k를 넣는다.
그런데 ball은 1,2이고, basket 1-2번 바구니의 인덱스는 0, 1이다. 따라서 basket[ball-1]을 해야한다.
리스트 형식이므로 새로운 값이 대입되면 이전 값을 덮는다.
4. 문제 풀이 제출은 리스트 형식이 아니므로 for문을 통해 리스트를 int 형식으로 변환한다.


'''
#%% 다시 풀기 
n = 5
m = 4
i_total = [1, 3, 1, 2]
j_total = [2, 4, 4, 2]
k_total = [3, 4, 1, 2]

basket = []
for n_idx in range(n): # n_idx = 1 / 2 / 3 / 4 / 5
    basket.append(n_idx*0) # basket = [0, 0, 0, 0, 0]

for mtd in range(m): # mtd = 0 / 1 / 2 / 3
    i = i_total[mtd] # i = 1 / 3 / 1 / 2
    j = j_total[mtd] # j = 2 / 4 / 4 / 2
    k = k_total[mtd] # k = 3 / 4 / 1 / 2
    for ball in range(i, j+1): # i=1, j=3, ball = 1, 2
        basket[ball-1] = k # basket = 0, 1 번째가 되어야하므로 ball에 -1을 한다.

for results in range(len(basket)):
    print(basket[results], end=' ') # 1 2 1 1 0
    print(type(basket[results])) # int
    
#%% 백준 제출용
n, m = map(int, input().split())

basket = []
for n_idx in range(n):
    basket.append(n_idx*0)

for mtd in range(m):
    i, j, k = map(int, input().split())
    for ball in range(i, j+1):
        basket[ball-1] = k
        
for results in range(len(basket)):
    print(basket[results], end=' ')

#%% 다른 사람 풀이
n,m=map(int,input().split())
basket=[0 for _ in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        basket[j]=c
for i in range(n):
    print(basket[i],end=' ')
