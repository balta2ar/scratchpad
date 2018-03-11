from pprint import pprint
from copy import deepcopy


def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] != 0:
        return field

    result = deepcopy(field)
    front = [(given_i, given_j)]

    def neighbors(x, y):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < num_rows and 0 <= j < num_cols:
                    yield (i, j)

    while front:
        x, y = front.pop()
        result[x][y] = -2
        for i, j in neighbors(x, y):
            value = result[i][j]
            if value == 0:
                front.append((i, j))

    pprint(result)
    return result


click(
    [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, -1, 1, 0]],
    3, 5, 0, 1)

click(
    [[-1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 1, 1],
     [0, 0, 1, -1]],
    4, 4, 1, 2)
