# 입력 = 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다.
# 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력 = 입력으로 주어진 숫자 N개의 합을 출력한다.

n = int(input())
a = map(int, input())
sum = 0
for i in a:
    sum += i
print(sum)