
# use -1 to mark a "non island" cell
def removeIslands(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = [matrix[0].copy()]

    # keep the last row for the last append operation
    last_row = matrix[m - 1].copy()

    # form a working stack by pushing all edge 1s' coordination
    stack = []
    for c in range(1, n - 1):
        # top edge
        if matrix[0][c] == 1:
            stack.append([0, c])

        # bottom edge
        if matrix[m - 1][c] == 1:
            stack.append([m-1, c])

    for r in range(1, m - 1):
        # left edge
        if matrix[r][0] == 1:
            stack.append([r, 0])
        # right edge
        if matrix[r][n - 1] == 1:
            stack.append([r, n - 1])

    while len(stack) > 0:
        coord = stack.pop()
        # check surrounding cells
        r = coord[0]
        c = coord[1]
        matrix[r][c] = -1
        # up
        if r > 0 and matrix[r - 1][c] == 1:
            stack.append([r-1, c])
        # down
        if r < m - 1 and matrix[r + 1][c] == 1:
            stack.append([r + 1, c])
        # left
        if c > 0 and matrix[r][c - 1] == 1:
            stack.append([r, c - 1])
        # right
        if c < n - 1 and matrix[r][c + 1] == 1:
            stack.append([r, c + 1])

    # now all non-island cell will be -1
    def collect_row_data(data):
        if data == -1:
            return 1
        return 0

    for r in range(1, m - 1):
        row = map(collect_row_data, matrix[r])
        result.append(row)

    result.append(last_row)

    return result


result = removeIslands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
])

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))
