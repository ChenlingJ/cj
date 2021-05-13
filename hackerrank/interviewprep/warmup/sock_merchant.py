from collections import defaultdict

def sock_merchant(socks: list[int]) -> int:
    color_counts = defaultdict(int)
    for sock in socks:
        color_counts[sock] += 1
    return sum(count // 2 for count in color_counts.values())

def main():
    _ = int(input())
    ar = list(map(int, input().split()))

    print(sock_merchant(ar))

if __name__ == "__main__":
    main()
