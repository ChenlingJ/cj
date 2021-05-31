def repeatedString(s, n):
    count = 0
    for c in s:
        if c == "a":
            count += 1
    count *= n // len(s)
    s_last = s[: n % len(s)]
    for c in s_last:
        if c == "a":
            count += 1
    return count


def main():
    s = input()
    n = int(input())
    print(repeatedString(s, n))


if __name__ == "__main__":
    main()
