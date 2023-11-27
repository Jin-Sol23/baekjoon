""" 문제 = 상근이는 매일 아침 알람을 듣고 일어난다.
알람을 듣고 바로 일어나면 다행이겠지만,
항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
바로 "45분 일찍 알람 설정하기"이다. """

""" 입력 = 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
그리고 이것은 현재 상근이가 설정한 알람 시간 H시 M분을 의미한다.
입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고,
끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다. """

# 출력 = 첫째 줄에 상근이가 창영이의 방법을 사용할 때,
# 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)

h, m = map(int, input().split())
if h > 0:
    if m < 45:
        print(h-1, m+15)
    elif m >= 45:
        print(h, m-45)
elif h == 0:
    if m < 45:
        print(h+23, m+15)
    elif m >= 45:
        print(h, m-45)

    
# 다른 사람 풀이
h,m = map(int,input().split())

if m < 45:
    if h == 0:
        h = 23
        m += 60
    else:
        h -= 1
        m += 60
print(h, m-45)