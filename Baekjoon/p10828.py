import sys

input=sys.stdin.readline
# input은 prompt message를 출력하고 \n을 rstirp()한 뒤 리턴해준다.
# sys.stdin.readline은 prompt message를 출력안하고 \n도 그냥 입력받아버린다.
# 과정에 차이가 있기 때문에 sys.stdin.readline이 input보다 빠른 것이다.


def solution(n):
    main_stack = []
    for i in range(n):
        cmd = input()
        if ("push" in cmd):
            cmd, num = cmd.split()
            num = int(num)
            stack_push(main_stack, num)
        elif ("pop" in cmd):
            print(stack_pop(main_stack))
        elif ("size" in cmd):
            print(stack_size(main_stack))
        elif ("empty" in cmd):
            print(stack_empty(main_stack))
        elif ("top" in cmd):
            print(stack_top(main_stack))

def stack_empty(stack):
    if (len(stack) == 0):
        return 1
    else:
        return 0

def stack_size(stack):
    return len(stack)

def stack_push(stack, n):
    stack.append(n)

def stack_pop(stack):
    if (stack_empty(stack) == 0):
        return stack.pop()
    else:
        return -1

def stack_top(stack):
    if (stack_empty(stack) == 0):
        return stack[-1]
    else:
        return -1

def main():
    n = int(input())
    solution(n)

if __name__ == "__main__":
    main()