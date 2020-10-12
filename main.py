import numpy


#grid = [[0, 0, 5, 0, 0, 1, 3, 9, 0],
#        [0, 0, 0, 0, 2, 0, 0, 0, 0],
#        [0, 0, 3, 0, 0, 8, 0, 0, 4],
#        [0, 0, 0, 0, 0, 7, 4, 0, 6],
#        [0, 9, 2, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 4, 5, 0, 0, 0, 1],
#        [1, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 8, 3],
#        [6, 4, 9, 0, 0, 0, 0, 0, 0]]

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def is_possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3)
    y0 = (y // 3)

    for i in range(y0, y0 + 3):
        for j in range(x0, x0 + 3):
            if grid[i][j] == n:
                return False
    return True


def solver():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    grid[y][x] = n
                    solver()
                    grid[y][x] = 0

                return



solver()
print(numpy.array(grid))
