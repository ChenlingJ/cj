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
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter
(in alphabetical order).

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
import itertools


def print_rangoli(size):
    print(rangoli(size))


def rangoli(size):
    if size == 1:
        return 'a'

    m = 4 * size - 3
    lines = []
    code = ord('a') - 1

    for i in itertools.chain(range(size), reversed(range(size - 1))):
        line = ''
        for j in range(i + 1):
            line += chr(code + size - j) + '-'
        for j in reversed(range(i)):
            line += chr(code + size - j)
            if j > 0:
                line += '-'
        lines.append(line.center(m, '-'))

    return '\n'.join(lines)


def rangoli2(size):
    grid_size = size * 2 - 1
    grid = [list('-' * grid_size) for _ in range(grid_size)]
    # [
    #     ['-', '-', '-', '-', '-'],
    #     ['-', '-', '-', '-', '-'],
    #     ['-', '-', '-', '-', '-'],
    #     ['-', '-', '-', '-', '-'],
    #     ['-', '-', '-', '-', '-'],
    #     ['-', '-', '-', '-', '-'],
    # ]
    # into
    # [
    #     ['-', '-', 'c', '-', '-'],
    #     ['-', 'c', 'b', 'c', '-'],
    #     ['c', 'b', 'a', 'b', 'c'],
    #     ['-', 'c', 'b', 'c', '-'],
    #     ['-', '-', 'c', '-', '-'],
    # ]
    for r in range(-(size - 1), size):
        for c in range(-(size - 1), size):
            # -2,  0 => 'c' == 'a'+2
            # -1, -1 => 'c' == 'a'+2
            # -1,  0 => 'b' == 'a'+1
            # -1,  1 => 'c' == 'a'+2
            #  0, -2 => 'c' == 'a'+2
            #  0, -1 => 'b' == 'a'+1
            #  0,  0 => 'a' == 'a'+0
            offset = abs(r) + abs(c)  # Manhattan distance from central 'a'.
            if offset < size:
                grid[r + size - 1][c + size - 1] = chr(ord('a') + offset)

    # rows = []
    # for row in grid:
    #     rows.append('-'.join(row))
    # return '\n'.join(rows)
    return '\n'.join('-'.join(row) for row in grid)


def main():
    n = int(input())
    print_rangoli(n)
