def jumpingOnClouds(c):
    i = 0
    step = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        step += 1
    return step


def main():
    n = int(input())
    c = list(map(int, input().strip().split()))
    print(jumpingOnClouds(c))


if __name__ == "__main__":
    main()
