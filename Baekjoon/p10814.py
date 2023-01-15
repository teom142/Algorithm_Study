def solution(n):
    arr = [0] * n
    min = 200
    for i in range(n):
        arr[i] = input().split(' ')
        arr[i][0] = int(arr[i][0])
        if (arr[i][0] < min):  # 최소 나이 찾기
            min = arr[i][0]
    # for i in range(min, 201):
        # if (arr.count())

    # arr.sort(key=lambda arr: arr[0])
    # print_arr(arr)
    # print(min)
    print(arr.count(min))


def print_arr(arr):
    for i in arr:
        print("{} {}".format(i[0], i[1]))


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
