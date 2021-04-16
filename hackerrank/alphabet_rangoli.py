"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    print(rangoli(size))


def rangoli(size):
    m = 4 * size - 3
    alp = ''
    alp1 = ''
    lines = []
    for i in range(1, size + 1):
        for j in range(0, i):
            alp += chr(96 + size - j) + '-'
        for k in range(0, i - 1):
            alp1 += chr(96 + size - k)
            if k != i - 2:
                alp1 += '-'
        result = alp + ''.join(reversed(alp1))
        # print(result.center(m, '-'))
        lines.append(result.center(m, '-'))
        alp = ''
        alp1 = ''

    for i in range(size - 1, 0, -1):
        for j in range(0, i):
            alp += chr(96 + size - j) + '-'
        for k in range(0, i - 1):
            alp1 += chr(96 + size - k)
            if k != i - 2:
                alp1 += '-'
        result = alp + ''.join(reversed(alp1))
        # print(result.center(m, '-'))
        lines.append(result.center(m, '-'))
        alp = ''
        alp1 = ''

    return '\n'.join(lines)


def rangoli2(size):
    grid_size = size*2 - 1
    grid = [list('-' * grid_size) for _ in range(grid_size)]

    for r in range(-(size-1), size):
        for c in range(-(size-1), size):
            # -2, 0 => c+2
            # -1, -1 => c+2
            # -1, 0 => c+1
            # -1, 1 => c+2
            # 0, -2 => c+2
            # 0, -1 => c+1
            # 0, 0 => c+0
            offset = abs(r) + abs(c)
            if offset < size:
                grid[r + size-1][c + size-1] = chr(ord('a') + offset)

    return '\n'.join('-'.join(row) for row in grid)


def main():
    n = int(input())
    print_rangoli(n)
