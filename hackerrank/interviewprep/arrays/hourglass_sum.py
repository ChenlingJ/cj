from math import inf


def hourglassSum(arr):
    # maximum = -63  # the lowest possible number
    # maximum = -float('inf')
    maximum = -inf
    for i in range(1, 5):
        for j in range(1, 5):
            hourglass_points = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, 0),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            new_sum = 0
            for y, x in hourglass_points:
                # += needs to have an initial value to be added to
                new_sum += arr[i + y][j + x]

            if new_sum >= maximum:
                maximum = new_sum
    return maximum


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
