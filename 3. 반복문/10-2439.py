# 입력 = 첫째 줄에 n이 주어진다.
# 출력 = 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
""" 출력 예시

    *
   **
  ***
 ****
*****

"""

n = int(input())

for i in range(1, n+1):
    result = f'{"*"*i:>{n}}'
    print(result)

# 다른 사람 풀이    
c = int(input())

for i in range(1, c+1):
    print(" "*(c-i) + "*"*i)