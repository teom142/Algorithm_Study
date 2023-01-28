import sys

input = sys.stdin.readline


def solution(n, k):
    value = []
    value_cnt = [0]*n
    ans = 0
    idx = 0
    for i in range(n):
        curr_val = int(input())
        if (curr_val <= k):
            value.append(curr_val)
            idx += 1
    idx -= 1
    while (idx >= 0 and k > 0):
        if (value[idx] <= k):
            value_cnt[idx] = k // value[idx]
            # // 연산으로 필요한 동전의 갯수 구함
            k %= value[idx]
            # % 연산으로 해당 동전의 가치만큼 k 뺄셈 연산
        else:
            idx -= 1
    for i in value_cnt:
        ans += i

    print(ans)


def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    solution(n, k)


if __name__ == "__main__":
    main()
