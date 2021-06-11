def solution(board: list, moves: list) -> int:
    moves = list(map(lambda x: x - 1, moves))
    # 열이 1번 부터니까 0으로 바꾼다.
    stack = []
    answer = 0
    for command in moves:
        # 기둥 번호 구해서
        for row in range(len(board)):
            if board[row][command] != 0:
                # 0인곳 까지 내려가서
                stack.append(board[row][command])
                # 스택에 넣은 다음
                board[row][command] = 0
                # 0으로 바꾼다음.
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            # 스택이 이상이고 끝값과 끝끝값이 같으면
            stack.pop(-1)
            stack.pop(-1)
            # 스택에 두개를 빼고
            answer += 2
            # 답을 2를 더해준다.
    return answer