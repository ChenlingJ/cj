HOURGLASS = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 1, 1],
]
HOURGLASS_INDEXES = [
    (row, col)
    for row in range(len(HOURGLASS))
    for col in range(len(HOURGLASS[row]))
    if HOURGLASS[row][col]
]


def hourglassSum(arr):
    return max(
        sum(arr[i + row][j + col] for row, col in HOURGLASS_INDEXES)
        for i in range(4)
        for j in range(4)
    )


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
