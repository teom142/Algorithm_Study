import sys

input = sys.stdin.readline


def solution(n, k):
    value = []
    value_cnt = [0]*n
    ans = 0
    i = 0
    for i in range(n):
        value.append(int(input()))
    idx = n - 1
    while (idx >= 0 and k > 0):
        if (value[idx] <= k):
            value_cnt[idx] += 1
            k -= value[idx]
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
