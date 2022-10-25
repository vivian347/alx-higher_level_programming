#!/usr/bin/python3
"""
contains pascal_triangle module
"""


def pascal_triangle(n):
    """returns a list of lists of ints repr the Pascal's triangle n"""
    my_triangle = []

    if n <= 0:
        return my_triangle
    my_triangle = [[1]]
    for x in range(1, n):
        m = [1]
        for y in range(1, x):
            m.append(my_triangle[x-1][y-1] + my_triangle[x-1][y])
        m.append(1)
        my_triangle.append(m)
    return my_triangle
