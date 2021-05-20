def hourglassSum(arr):
    hourglass_points = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 0),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    return max(
        sum(arr[i + y][j + x] for y, x in hourglass_points)
        for i in range(1, 5)
        for j in range(1, 5)
    )


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
