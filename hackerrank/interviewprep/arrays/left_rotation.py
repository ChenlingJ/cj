# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


def rotLeft(a: list[int], d: int) -> list[int]:
    d %= len(a)
    return a[d:] + a[:d]


def main():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(*rotLeft(a, d))


if __name__ == "__main__":
    main()
