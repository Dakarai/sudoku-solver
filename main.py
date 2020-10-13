def form_grid(puzzle_string):
    global grid
    for i in range(0, len(puzzle_string), 9):
        row = puzzle_string[i: i + 9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)
    print_grid()


def print_grid():
    global grid
    for row in grid:
        print(row)


def possible(row, col, n):
    global grid
    for i in range(9):
        if grid[row][i] == n or grid[i][col] == n:
            return False
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[square_row + i][square_col + j] == n:
                return False
    return True


def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1, 10):
                    if possible(row, col, digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0
                return
    print("\n Solution: \n")
    print_grid()


input_string = "002000000035070000000000098080600040670810000000000000000754000000000069200003080"
grid = []
form_grid(input_string)
solve()
