# 입력 = 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
# 출력 = 각 테스트 케이스마다 A+B를 출력한다.

# EOF(End of file)

try:
    while True:
        a, b = map(int, input().split())
        print(a+b)
except:
    pass
    
# 다른 사람 풀이
while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break