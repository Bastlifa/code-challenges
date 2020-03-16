def sudoku2(grid):
    box_sets = {k: set() for k in range(len(grid))}
    for i, row in enumerate(grid):
        row_set = set()
        col_set = set()
        for j, col in enumerate(grid):
            if grid[i][j] != '.':
                if grid[i][j] in row_set:
                    return False
                else:
                    row_set.add(grid[i][j])
                
                if grid[i][j] in box_sets[3*(i//3) + j//3]:
                    return False
                else:
                    box_sets[3*(i//3) + j//3].add(grid[i][j])
            
            if grid[j][i] != '.':
                if grid[j][i] in col_set:
                    return False
                else:
                    col_set.add(grid[j][i])

    return True