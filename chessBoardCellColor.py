def chessBoardCellColor(cell1, cell2):
    row1 = int(cell1[1])
    col1 = ord(cell1[0])
    row2 = int(cell2[1])
    col2 = ord(cell2[0])

    return ((row2 + col2) - (row1 + col1)) % 2 == 0 
