# Constant value does not change between invocations of hourglassSum
# Constants are usually defined on a module level and written in all capital letters with
# underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

# The 2D shape of an hourglass. 1 = part of the hourglass, 0 = not in the hourglass.
HOURGLASS = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 1, 1],
]

HOURGLASS_POINTS = []
for row in range(3):
    for col in range(3):
        if HOURGLASS[row][col] == 1:
            HOURGLASS_POINTS.append((row, col))


def hourglassSum(arr):
    return max(
        sum(
            arr[i + row][j + col] * HOURGLASS[row][col]
            for row in range(3)
            for col in range(3)
        )
        for i in range(4)
        for j in range(4)
    )


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
