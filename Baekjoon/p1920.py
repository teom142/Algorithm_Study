import bisect as bi

def solution(n):
    n_list = int_list_input()
    n_list.sort()
    m = int(input())
    m_list = int_list_input()
    for i in m_list:
        if(bi.bisect_right(n_list, i) - bi.bisect_left(n_list, i) != 0):
            print("1")  # 원소의 개수가 0이 아니면 존재한다고 판단
        else:
            print("0")

def int_list_input():
    lis = input().split()
    for i in lis:
        i = int(i)
    return lis

def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
