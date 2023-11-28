# 문제 = n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력 = 첫째 줄에 n 입력
# 출력 = 1~n까지 합 출력

n = int(input())
sum=0
for i in range(1, n+1):
    sum += i
print(sum)