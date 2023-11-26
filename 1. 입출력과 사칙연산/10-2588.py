# 입력 = 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 입력됨
# 출력 = 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값 출력

x = input() # 472
y = list(input()) # 385

sec_index = y[2]
thr = int(x)*int(sec_index)

fir_index = y[1]
four = int(x) * int(fir_index)

zer_index = y[0]
fiv = int(x) * int(zer_index)

print(thr) # 2360
print(four) # 3776
print(fiv) # 1416
print(thr + (four*10) + (fiv*100)) # 181720



a, b = int(input()), input()

print(a * (int(b[2])))
print(a * (int(b[1])))
print(a * (int(b[0])))
print(a * int(b))