# 문제 : 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.

# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 반복 횟수 R, 문자열 S가 공백으로 구분되어 주어진다.

# 출력 : 각 테스트 케이스에 대해 P를 출력한다.

s = int(input())

for i in range(s):
    a, b = input().split()
    c = []
    for j in range(len(b)):
        result = int(a)*b[j]
        c += result
    print(''.join(c))


# GPT 답변
s = int(input())

for i in range(s):
    a, b = input().split()
    result = ''.join(int(a) * char for char in b)
    print(result)


# 다른 사람 풀이_1
T = int(input())

ans = ""
for i in range(T):
    rep, word = input().split()
    rep = int(rep)
    for j in range(len(word)):
        for k in range(rep):
            ans += word[j]
    ans += " "

for i in range(T):
    print(ans.split(" ")[i])


# 다른 사람 풀이_2
count = int(input())
r_result = ""
for i in range(count):
    a = input().split()
    String = a[1]
    for i in range(int(len(String))):
        r_result = r_result + String[i]*int(a[0])
    print(r_result)
    r_result = ""