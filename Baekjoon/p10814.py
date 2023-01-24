def solution(n):
    arr = [0] * n
    for i in range(n):
        arr[i] = input().split(' ')
        arr[i][0] = int(arr[i][0])
    arr.sort(key=lambda arr: arr[0])
    for i in arr:
        print("{} {}".format(i[0], i[1]))


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
