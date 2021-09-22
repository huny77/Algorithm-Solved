import sys
sys.stdin = open("input.txt")

while True:
    word = input()
    if word == '.': break
    stack = []
    for i in word:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if stack and i == ")" and stack[-1] == "(" or i == "]" and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")





# word = "e(e)e("
# stack = []
#
# for i in word:
#     if not stack and (i == "(" or i == ")"):
#         stack.append(i)
#     elif i == "(":
#         stack.append(i)
#     elif stack and stack[-1] == "(" and i == ")":
#         stack.pop(-1)
# if stack:
#     print("False")
# else:
#     print("True")


