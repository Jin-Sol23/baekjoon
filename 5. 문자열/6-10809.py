'''
첫째 줄에 단어 S가 주어진다.
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치,
... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
'''
# 입력 : baekjoon
# 출력 : 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

#%%
# 소문자 a = 97, z= 122
s = input()
a = ord("a")
z = ord("z")

for i in range(97, 123):
    for j in range(chr(s)):
        if i == j:
            i = 
            print(len(i))
    print(i)

#%% 성공!!
s = input() # 'baekjoon'
aa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in aa:
    for j in range(len(s)):
        if s[j] in i:
            b = j
#            b = s.index(s[j])
            break
#            print(a, end=' ')
        else:
            b = -1    
    print(b, end=' ')

#%% chat GPT 
s = 'baekjoon'
for j in range(97, 123):
    found = False
    for i in range(len(s)):
        if s[i] == chr(j):
            # j = i
            found = True
            break
    if not found: # 위의 found가 False니까 not found면 True??
        i = -1
    print(i, end=' ')

# found sw 의 역할
# found sw 없이 이 문제 풀어보기
#%%

s = 'baekjoon'
for j in range(97, 123):
    # found = False
    for i in range(len(s)):
        
        print(chr(j),j, s[i],  s[i] == chr(j), i)
        
        # if s[i] == chr(j):
            # j = i
            # found = True
#            break
    # if not found:
    #     i = -1
    # print(i, end=' ')

#%%
# flag 변수
flag=True
print(flag) # True
print(type(flag)) # bool

# flag=not flag
if flag:
    print("True 입니다.")
else:
    print("False 입니다.")





