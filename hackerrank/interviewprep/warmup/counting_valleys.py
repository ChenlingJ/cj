from itertools import accumulate


def countingValleys(steps, path):
    number_path = []
    for step in path:
        if step == "U":
            number_path.append(1)
        elif step == "D":
            number_path.append(-1)
    elevations = list(accumulate(number_path))  # itertools always return iterators
    count = 0
    for i in range(len(elevations)):
        if (
            elevations[i] == 0 and elevations[i - 1] == -1
        ):  # The first elevation can never be zero.
            count += 1
    return count


def main():
    steps = int(input().strip())
    path = input()  # path is a string containing U's and D's
    result = countingValleys(steps, path)
    print(result)


if __name__ == "__main__":
    main()
