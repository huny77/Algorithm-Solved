import sys
sys.stdin = open("input.txt")

# 입력단
N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))
# dict으로 변환할 것을 갖고 있는다.
dict_temp = dict()

# 일단 N_arr을 돌면서 dict에 다 넣고, 갯수를 센다.
for i in N_arr:
    if i in dict_temp:
        dict_temp[i] += 1
    else:
        dict_temp[i] = 1

# 그리고 M_arr을 돌면서 만약 겹치는 것이 있으면 그 자리에 넣고
# 아니면 0을 넣는다.
ans = []
for i in M_arr:
    if i in dict_temp:
        ans.append(dict_temp[i])
    else:
        ans.append(0)

# 리스트가 없는 형태로 출력
print(*ans)