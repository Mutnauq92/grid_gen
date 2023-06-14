import random

def grid(rows, cols):
    """Returns a grid containing grids according to specified rows and cols
    
    :param rows: Number of rows each grid will have
    :type rows: int

    :param cols: Number of columns a each grid will have
    :type cols: int

    :param n: Number of grids to create and return
    :type: int

    :return: Grid list
    :rtype: 2D list
    
    """
    
    # make a list of choices to use as mine spots
    choices = ["#", "-"]
    # create a temporary list containing strings according given rows and columns 
    grid = []
    # create a grid according to given rows and columns
    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(random.choice(choices))
        grid.append(temp)

    to_file("logs.txt", grid)
    return grid

def grids(rows, cols, n=1):
    """Returns a grid containing grids according to specified rows and cols
    
    :param rows: Number of rows each grid will have
    :type rows: int

    :param cols: Number of columns a each grid will have
    :type cols: int

    :param n: Number of grids to create and return
    :type: int

    :return: Grid list
    :rtype: 2D list
    
    """
    grid_list = []

    try:
        while len(grid_list) < n:
            new_grid = grid(rows, cols)
            grid_list.append(new_grid)

        return grid_list
    except ValueError as ve:
        print("Invalid input !!!")
    except IndexError as ie:
        print("Please enter integer about 0")

def to_file(filename, grid):
    """This function writes the generated grid to a text file."""
    try:
        if not isinstance(grid[0][0], list):
            rows = len(grid)
            cols = len(grid[0])
            rows_cols = f"\n{rows,cols}"

            grid_string = ""
            for i in grid:
                grid_string += "".join(map(str, i))
            
            with open(filename, "a") as f:
                f.write(f"{rows_cols}|{grid_string}")
        else:
            for each_grid in grid:
                rows = len(each_grid)
                cols = len(each_grid[0])
                rows_cols = f"\n{rows,cols}"

                grid_string = ""
                for i in each_grid:
                    grid_string += "".join(map(str, i))

                with open(filename, "a") as f:
                    f.write(f"{rows_cols}|{grid_string}")
    except ValueError as ve:
        print("Invalid input !!!")
    except IndexError as ie:
        print("Please enter integer about 0")

def from_file(filename, begin=1, limit=None):
    """ If the value of argument n is not specified, all grids in history file will be returned

    :param filename: The name of the file to read from
    :type text: Text file type

    :param n: Number of grids to read
    :type str and tuple: rows_cols tuple and grid string

    """
    
    grids = []

    with open(filename, "r") as f:
        # skip the first line in the text file, it is used for headings
        next(f)
        for line in f:
            cleaned = line.strip("\n").split("|")
            rows, cols = eval(cleaned[0])
            temp_grid = []
            grid = []
            [temp_grid.append(i) for i in cleaned[1]]
            count = 0
            for i in range(rows):
                temp = []
                for j in range(cols):
                    temp.append(temp_grid[count])
                    count += 1
                grid.append(temp)
            grids.append(grid)

    if begin is None and limit is None:
        return grids[begin - 1:]
    else:
        return grids[begin - 1: limit]
