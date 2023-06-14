import grid_gen
from tabulate import tabulate

def sweeper(grid):
    """
    Returns an updated grid with number of mines around each spot

    :param grid: Grid / 2D List

    :rtype grid: 2D List / Grid
    :return: Updated Grid
    """

    # set length of the grid as number of rows
    rows = len(grid)
    # set length of the first row as number of columns
    cols = len(grid[0])
    # mine spots around the current spots, represented by tuples.
    spots = [
        (1,0), (-1,0), (0, -1), (0, 1),
        (-1,-1), (-1,1), (1,-1), (1,1)
    ]
    # create a temporary grid to update later with number of mines
    temp_grid = [[0] * cols for row in range(rows)]

    # iterate over rows
    for i in range(rows):
        # iterate over columns
        for j in range(cols):
            # check the current spot if it is minre free
            if grid[i][j] == "-":
                # initialize a counter to keep track of mines around the current spot
                count = 0
                # iterate over the 8 spots around the current spot
                for x, y in spots:
                    ni, nj = x + i, y + j
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "#":
                        count += 1
                    temp_grid[i][j] = count
    return temp_grid

# create a variable and assign imported grid generation
# read information from any text file.
grids = grid_gen.from_file("logs.txt", 22, 25)
grid = grids[0]
result = sweeper(grid)
print(tabulate(grid, tablefmt="simple_grid"))
print(tabulate(result, tablefmt="simple_grid"))
