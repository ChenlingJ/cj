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
row = None
col = None
for row in range(3):
    for col in range(3):
        if HOURGLASS[row][col] == 1:
            # Pass the tuple (row, col) to the append method
            # The append method doesn't have a return value, but it modifies
            # the HOURGLASS_POINTS list. This is known as a "side effect" because it
            # does something aside from returning a value.
            HOURGLASS_POINTS.append((row, col))


# hourglass_points = [
#     (-1, -1),
#     (-1, 0),
#     (-1, 1),
#     (0, 0),
#     (1, -1),
#     (1, 0),
#     (1, 1),
# ]

# List comprehension:
# [ expression for var1 in iterator1 for var2 in iterator2 if condition ]
# row and col are local to the comprehension, and are not available for the whole file.
# HOURGLASS_POINTS = [
#     (row, col)
#     for row in range(3)
#     for col in range(3)
#     if HOURGLASS[row][col] == 1
# ]

# HOURGLASS_POINTS = []
# # h is a generator expression, and is lazily evaluated
# h = (
#     HOURGLASS_POINTS.append((row, col))
#     for row in range(3)
#     for col in range(3)
#     if HOURGLASS[row][col] == 1
# )
# list(h) returns [None, None, None, None, None, None, None] and before this HOURGLASS_POINTS remains empty.


# def three_powers():
#     n = 1
#     while True:
#         yield n
#         yield n * n
#         yield n * n * n
#         n += 1

#
# def powers(p):
#     if p <= 0:
#         return
#     n = 1
#     while True:
#         x = 1
#         x *= n
#         for i in range(p):
#             yield x
#             x *= n
#         n += 1


# def powers(p):
#     if p <= 0:
#         return
#     n = 1
#     while True:
#         x = 1
#         for i in range(p):
#             x *= n
#             yield x
#         x *= n
#         n += 1


def hourglassSum(arr):
    return max(
        sum(
            # This is a generator expression, which is similar to
            # a list comprehension but is evaluated lazily.
            # The opposite of lazy evaluation is eager evaluation, where
            # all the values are computed in advance.
            arr[i + row][j + col]
            for row, col in HOURGLASS_POINTS
            # The squiggly lines under row and col indicate that they've
            # shadowed the global names row and col, defined above.
        )
        for i in range(4)
        for j in range(4)
    )


def main():
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    print(hourglassSum(arr))


if __name__ == "__main__":
    main()
