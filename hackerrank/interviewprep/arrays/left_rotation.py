# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


def rotLeft(a: list[int], d: int) -> list[int]:
    # recursion: If d is negative, recursion will run infinitely;
    # takes memory to call a function and this puts an upper limit on d
    # if d <= 0:
    #     return a
    # b = []
    # for i in range(1, len(a)):
    #     b.append(a[i])
    # b.append(a[0])
    # return rotLeft(b, d-1)

    d %= len(a)
    # b = []
    # for i in range(d, len(a)):
    #     b.append(a[i])
    # # if d = 0, for loop iterates an empty iterator, and will not run.
    # for i in range(0, d):
    #     b.append(a[i])
    # return b

    # return a[d:len(a)] + a[0:d]
    return a[d:] + a[:d]


if __name__ == "__main__":
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(*rotLeft(a, d))
