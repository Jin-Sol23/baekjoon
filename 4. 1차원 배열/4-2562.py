# 입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
# 출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

m = []
for i in range(9):
    n = int(input())
    m += [n]  # n에 []를 해아함. 또는 "m.append(n)" 도 가능
    m_max = max(m)
print(m_max)
print(m.index(m_max)+1)
