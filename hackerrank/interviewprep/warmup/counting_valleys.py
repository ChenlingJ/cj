def countingValleys(steps, path):
    altitude = 0
    valley_count = 0
    for step in path:
        if step == "U":
            altitude += 1
            if altitude == 0:
                # If we just got to sea level by going uphill, we must have been in a valley.
                valley_count += 1
        elif step == "D":
            altitude -= 1
    return valley_count


# input is DDUU
# elevations: -1 -2 -1 0 (valley ends)


def main():
    steps = int(input().strip())
    path = input()  # path is a string containing U's and D's
    result = countingValleys(steps, path)
    print(result)


if __name__ == "__main__":
    main()
