# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:27:14 2023

@author: adam
"""

# 배수와 약수

# 문제 : 입력은 여러 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다.
# 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

# 출력 :  테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를,
# 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    elif b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')