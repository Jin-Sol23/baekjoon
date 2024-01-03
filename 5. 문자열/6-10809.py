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
#%%
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





