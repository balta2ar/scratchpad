from copy import deepcopy

def pprint(items):
    for line in items:
        print(''.join(['%04s' % cell for cell in line]))


def rotate_copy(items, n):
    print(items)
    result = deepcopy(items)

    for i in range(n):
        for j in range(n):
            new_row = j
            new_col = n - i - 1
            # print(i, j, new_row, new_col)
            result[new_row][new_col] = items[i][j]
            # current column => new row
            # N - current_row + 1 => new column

    print(result)


def rotate_inplace(items, n):
    pprint(items)

    def rotate_coord(i, j):
        return j, n - i - 1

    def carry(i, j, depth):
        source_value = items[i][j]
        dest_i, dest_j = rotate_coord(i, j)
        if depth != 0:
            carry(dest_i, dest_j, depth-1)
        items[dest_i][dest_j] = source_value

        # We need to rotate roughly a quarter of the matrix as follows:
        #
        #    <............>
        #    1   2   3   4   5
        #       <.....>
        #    6   7   8   9  10
        #   11  12  13  14  15
        #   16  17  18  19  20
        #   21  22  23  24  25

    for i in range(n//2):
        for j in range(i, n-i-1):
            print(items[i][j], end=',')
            carry(i, j, 4)
        print()

    pprint(items)


# rotate_copy(
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]],
#     3)

# rotate_inplace(
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]],
#     3)

# rotate_inplace(
#     [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]],
#     4)

rotate_inplace(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]],
    5)
