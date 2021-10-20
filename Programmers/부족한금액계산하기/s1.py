def solution(price, money, count):
    temp = 0
    # 결국 1부터 돌리는게 편함
    # 카운트 만큼 돌렸을 때, price 금액을 temp에 더해주기
    for i in range(1, count + 1):
        temp += price * i
    # 만약에 temp가 money보다 크다면 0
    if temp <= money:
        answer = 0
    # 작으면 temp-money값
    else:
        answer = temp - money

    return answer