"""
http://practice.geeksforgeeks.org/problems/x-total-shapes/0#ExpectOP

Given N * M string array of O's and X's
Return the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

Example (1):

OOOXOOO
OXXXXXO
OXOOOXO

answer is 1 , shapes are  :
(i)     X
    X X X X
    X     X
 

Example (2):

XXX
OOO
XXX

answer is 2, shapes are
(i)  XXX

(ii) XXX

Input:
The first line of input takes the number of test cases, T.
Then T test cases follow. Each of the T test cases takes 2 input lines.
The first line of each test case have two integers N and M.The second line of N space separated strings follow which indicate the elements in the array.

Output:

Print number of shapes.

Constraints:

1<=T<=100

1<=N,M<=50

Example:

Input:
2
4 7
OOOOXXO OXOXOOX XXXXOXO OXXXOOO
10 3
XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO

Output:
4
6


"""
from sys import stdin
from io import StringIO
from queue import deque


TEST1 = '''6
4 7
OOOOXXO OXOXOOX XXXXOXO OXXXOOO
10 3
XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO
1 1
O
2 2
OO OX
1 8
OOOXOOOX
8 1
O X O O X O O O
'''
TEST1_OUTPUT = '\n'.join(['4', '6', '0', '1', '2', '2'])

DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def run_bfs(field, visited, start_row, start_col, n, m, value):
    front = deque()
    front.append((start_row, start_col))

    def neighbors(x, y):
        result = []
        for dx, dy in DELTA:
            nrow, ncol = x+dx, y+dy
            if 0 <= nrow < n and 0 <= ncol < m and field[nrow][ncol] == 'X':
                result.append((nrow, ncol))
        return result

    while front:
        row, col = front.popleft()
        visited[row][col] = value
        for nrow, ncol in neighbors(row, col):
            if not visited[nrow][ncol]:
                front.append((nrow, ncol))


def solve_field(field, n, m):
    visited = [[0] * m for _ in range(n)]

    num_islands = 0
    for row in range(n):
        for col in range(m):
            if field[row][col] == 'X' and visited[row][col] == 0:
                num_islands += 1
                run_bfs(field, visited, row, col, n, m, num_islands)

    return num_islands


def solve_bfs(input):
    result = []
    num_tests = int(input.readline().strip())

    for test_num in range(num_tests):
        n, m = input.readline().strip().split()
        n, m = int(n), int(m)
        field = input.readline().strip().split()
        result.append(str(solve_field(field, n, m)))

    return '\n'.join(result)


def test_bfs():
    output = solve_bfs(StringIO(TEST1))
    assert TEST1_OUTPUT.strip().split() == output.strip().split()


if __name__ == '__main__':
    print(solve_bfs(stdin))