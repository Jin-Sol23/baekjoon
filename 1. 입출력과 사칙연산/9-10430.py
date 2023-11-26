# 입력 = 첫 줄에 A,B,C가 순서대로 주어진다
# 출력 = 첫 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C)%C), 셋째 줄에 (A*B)%C, 넷째줄에 ((A%C)*(B%C)%C)를 출력

a, b, c = input().split() # 5 8 4
a = int(a)
b = int(b)
c = int(c)

print((a+b)%c) # 1
print(((a%c)+(b%c))%c) # 1
print((a*b)%c) # 0
print(((a%c)*(b%c))%c) # 0