import numpy


grid = [[0, 0, 5, 0, 0, 1, 3, 9, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 8, 0, 0, 4],
        [0, 0, 0, 0, 0, 7, 4, 0, 6],
        [0, 9, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 5, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 3],
        [6, 4, 9, 0, 0, 0, 0, 0, 0]]

#grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#        [6, 0, 0, 1, 9, 5, 0, 0, 0],
#        [0, 9, 8, 0, 0, 0, 0, 6, 0],
#        [8, 0, 0, 0, 6, 0, 0, 0, 3],
#        [4, 0, 0, 8, 0, 3, 0, 0, 1],
#        [7, 0, 0, 0, 2, 0, 0, 0, 6],
#        [0, 6, 0, 0, 0, 0, 2, 8, 0],
#        [0, 0, 0, 4, 1, 9, 0, 0, 5],
#        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def is_possible(board, y, x, n):

    for i in range(0, 9):
        if board[y][i] == n and x != i:
            return False

    for i in range(0, 9):
        if grid[i][x] == n and y != i:
            return False

    box_x = x // 3
    box_y = y // 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if grid[i][j] == n and x != j and y != i:
                return False
    return True


def solver(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    else:
        y, x = empty_cell

    for i in range(1, 10):
        if is_possible(board, y, x, i):
            board[y][x] = i

            if solver(board):
                return True

            board[y][x] = 0

    return False


def find_empty_cell(board):
    for y in range(0, 9):
        for x in range(0, 9):
            if board[y][x] == 0:
                return (y, x)


grid = solver(grid)
print(numpy.array(grid))
