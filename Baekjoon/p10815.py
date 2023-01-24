import bisect as bi

def solution(n):
    card = []
    serch_val = []
    card = input().split()
    for i in card:
        i = int(i)
    card.sort()
    m = int(input())        # 어따쓰지...
    serch_val = input().split()
    for i in serch_val:
        i = int(i)
    for i in serch_val: # right - left를 하면 해당 원소의 개수가 나온다.
        print(bi.bisect_right(card, i) - bi.bisect_left(card, i), end=' ')

def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
