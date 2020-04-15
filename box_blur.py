def boxBlur(image):
    rows = len(image)
    cols = len(image[0])

    output = []

    for i in range(1, rows - 1):
        row = []
        for j in range(1, cols - 1):
            avg =   (image[i-1][j-1] +
                    image[i-1][j] +
                    image[i-1][j+1] +
                    image[i][j-1] +
                    image[i][j] +
                    image[i][j+1] +
                    image[i+1][j-1] +
                    image[i+1][j] +
                    image[i+1][j+1]) // 9
            row.append(avg)
        output.append(row)
    return output
