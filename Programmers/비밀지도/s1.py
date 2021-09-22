def solution(n, arr1, arr2):
    # answer을 ''으로 초기화 (바로바로 넣어주기 위해)
    answer = ['' for _ in range(n)]
    for i in range(n):
        # 비트연산자 or을 이용해서 바로 2개의 arr을 합친 것을 구함
        # bin 함수를 사용하기 때문에 앞에 2개 슬라이싱
        temp = bin(arr1[i] | arr2[i])[2:]

        # 만약 n보다 행이 작으면 앞에 '0'을 붙여줌
        while len(temp) < n:
            temp = '0' + temp

        # 합친 지도의 0은 ' '로, 1은 '#'으로 answer에 넣어줌
        for j in range(n):
            if temp[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'

    return answer