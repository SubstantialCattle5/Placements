def tree_conversion(tree) : 
    if tree== "*" : 
        return 1 
    return 0 
def solution(rows,cols,grid,queries) : 
    preFixGrid = [[0] * cols for _ in range(rows)] 
    # inital setup 
    preFixGrid[0][0] = queries[0][0]
    for i in range(rows) :
        for j in range(cols) :
            if i ==0 and j == 0 : 
                preFixGrid[i][j] = tree_conversion(grid[i][j])
            elif i == 0 : 
                preFixGrid[i][j] = preFixGrid[i][j-1] + tree_conversion(grid[i][j])
            elif j == 0 : 
                preFixGrid[i][j] = preFixGrid[i-1][j] + tree_conversion(grid[i][j])
            else : 
                preFixGrid[i][j] = preFixGrid[i-1][j] + preFixGrid[i][j-1] - preFixGrid[i-1][j-1] + tree_conversion(grid[i][j])

    for i in range(len(queries)) : 
        from_row,from_col,to_row,to_col = queries[i]
        ans = preFixGrid[to_row][to_col] - preFixGrid[from_row-1][to_col] - preFixGrid[to_row][from_col-1] + preFixGrid[from_row-1][from_col-1]
        print(ans)

if __name__ == "__main__":
    
# Dimensions of the grid
    rows, cols = 4, 3

# The grid itself
    grid = [
    [".", "*", ".","."],
    ["*", ".", "*", "*"],
    ["*", "*", ".", "."],
    ["*", "*", "*", "*"]
    ]

# Queries (each query is represented as a tuple of (row1, col1, row2, col2))
    queries = [
    (2, 2, 3, 4),
    (3, 1, 3, 1),
    (1, 1, 2, 2)
    ]
    
    solution(rows,cols,grid,queries)
