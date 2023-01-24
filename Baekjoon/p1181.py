import sys

input=sys.stdin.readline

def solution(n):
    word = []
    for i in range(n):
        word.append(input().split("\n"))
        word[i][1] = len(word[i][0])

    word.sort(key = lambda x: (x[1], x[0])) 
        # 1번 인덱스 값을 우선 기준으로 정렬
        # 1번 인덱스 값이 같으면 2번 인덱스 값을 다음 기준으로 정렬
    i = 0
    while(i < n):
        print(word[i][0])
        while (i < n-1 and word[i][0] == word[i + 1][0]):
            i += 1
        i += 1

def main():
    n = int(input())
    solution(n)

if __name__ == "__main__":
    main()
