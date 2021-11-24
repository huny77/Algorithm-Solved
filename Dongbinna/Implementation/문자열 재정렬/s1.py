import sys
sys.stdin = open("input.txt")

words = list(input())
ans = []
temp = 0

# 문자이면 더해주고 정렬, 숫자면 더해준다
for word in words:
    if word.isalpha():
        ans.append(word)
        ans.sort()
    else:
        temp += int(word)

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if temp != 0:
    ans.append(str(temp))

# 최종 결과물
print(''.join(ans))



