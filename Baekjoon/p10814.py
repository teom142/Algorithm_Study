def solution(n):
    arr = [0] * n
    for i in range(n):
        arr[i] = input().split(' ')
    print(arr)


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
