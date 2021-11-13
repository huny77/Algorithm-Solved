

s = "one4seveneight"
# 정답용 초기화
answer = ''
# 중간에 문자열 완성용 초기화
string = ''
# 딕셔너리
words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# s를 반복했을 때
for i in s:
    # 숫자면 answer에 바로 더하고
    if i.isdigit():
        answer += i
    # 문자면 다음 방법을 사용한다.
    else:
        # 먼저 중간 저장에 단어를 넣고 단어가 다 완성되면
        string += i
        # 딕셔너리 키 값과 비교해서 해당 값을 str로 넣어줌
        if string in words.keys():
            answer += str(words[string])
            # 그리고 다시 초기화해야 다음 값도 검색 가능
            string = ''
print(int(answer))