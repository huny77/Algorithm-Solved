import sys
sys.stdin = open("input.txt")

# list 형태로 입력 받기
s = list(input())
ans = []
temp = 0

for i in s:
    # 숫자가 아닌 문자면 ans에 append
    if i.isalpha():
        ans.append(i)
    # 숫자면 temp에 더해서 갖고 있기
    else:
        temp += int(i)
# 문자를 오름차순 정렬
ans.sort()

# 출력
print("".join(ans)+str(temp))