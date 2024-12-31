def is_valid(yy, row, col, num):
    for i in range(9):
        if yy[row][i] == num:
            return False
    for i in range(9):
        if yy[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if yy[start_row + i][start_col + j] == num:
                return False
    return True
def solve_sudoku(yy):
    for row in range(9):
        for col in range(9):
            if yy[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(yy, row, col, num):
                        yy[row][col] = num
                        if solve_sudoku(yy):
                            return True
                    yy[row][col] = 0
                return False
    return True
yy = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve_sudoku(yy)
for row in yy:
    print(row)