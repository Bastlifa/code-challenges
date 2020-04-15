def minesweeper(matrix):
    if len(matrix) == 0:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])

    output = []

    for i in range(rows):
        row = []
        for j in range(cols):
            val = 0

            if i > 0:
                if j > 0:
                    val += matrix[i-1][j-1]
                val += matrix[i-1][j]
                if j < cols - 1:
                    val += matrix[i-1][j+1]

            if j > 0:
                val += matrix[i][j-1]
            # val += matrix[i][j]
            if j < cols - 1:
                val += matrix[i][j+1]

            if i < rows - 1:
                if j > 0:
                    val += matrix[i+1][j-1]
                val += matrix[i+1][j]
                if j < cols - 1:
                    val += matrix[i+1][j+1]

            row.append(val)
        output.append(row)

    return output
