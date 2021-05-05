# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
#
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


def read_lines(n: int) -> list[str]:
    """
    Read and return `n` lines of input.
    """
    return [input() for _ in range(n)]


def parse_commands(lines: list[str]) -> list[tuple[str, list[int]]]:
    """
    Process a list of `lines` and turn into command tuples `(command, args)`.
    """
    result = []
    for line in lines:
        command, *args = line.split()
        args = list(map(int, args))
        result.append((command, args))
    return result


def run_commands(commands: list[tuple[str, list[int]]]) -> list[str]:
    arr = []
    output = []
    methods = {
        "insert": arr.insert,
        "remove": arr.remove,
        "append": arr.append,
        "sort": arr.sort,
        "pop": arr.pop,
        "reverse": arr.reverse,
    }
    for command, args in commands:
        if command == "print":  # print is not a method of arr.
            output.append(str(arr))
        else:
            methods[command](*args)
    return output


if __name__ == "__main__":
    N = int(input())
    print("\n".join(run_commands(parse_commands(read_lines(N)))))
