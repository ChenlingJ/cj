from math import inf


def hourglassSum(arr):
    # maximum = -63  # the lowest possible number
    # maximum = -float('inf')
    maximum = -inf
    for i in range(1, 5):
        for j in range(1, 5):

            new_sum = (
                arr[i - 1][j - 1]
                + arr[i - 1][j + 0]
                + arr[i - 1][j + 1]
                + arr[i + 0][j + 0]
                + arr[i + 1][j - 1]
                + arr[i + 1][j + 0]
                + arr[i + 1][j + 1]
            )
            if new_sum >= maximum:
                maximum = new_sum
    return maximum


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
