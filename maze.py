# MAZE.PY
from cell import Cell  # import the Cell class
import time  # for time.sleep()
import random  # for random.seed, random etc

# holds all the cells in a 2d grid
class Maze: 
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed=None
        ):
        self._cells = []  # initiate cell list to be filled
        self._x1 = x1  # x coord of topleft of maze
        self._y1 = y1  # y coord of topleft of maze
        self._num_rows = num_rows  # no of rows in maze
        self._num_cols = num_cols  # no of cols in maze
        self._cell_size_x = cell_size_x  # width of each cell in pixels
        self._cell_size_y = cell_size_y  # height of each cell in pixels
        self._win = win  # window objt where maze is drawn
        if seed:  # if seed True
            random.seed(seed)  # randomise it
        # a FIXED seed ensures we always get the same "random" numbers (helps with debugging)

        self._create_cells()  # calls the cell creation method
        self._break_entrance_and_exit()  # create enter/exit cells
        self._break_walls_r(0, 0)  # break walls inside the maze
        self._reset_cells_visited()  # resets visited flag to allow solving maze after


    # fills all cells
    # were drawing left to right
    # fill columns first, then do rows of columns
    def _create_cells(self):
        # Build the 2D grid structure column by column
        for i in range(self._num_cols):
            col_cells = []  # Start a new column
            for j in range(self._num_rows):
                cell = Cell(self._win)  # Create a cell that can draw itself
                col_cells.append(cell)  # Fill each row of a column
            self._cells.append(col_cells)  # THEN Add completed column to the grid
        
        # After creating all cells, draw each one in its correct position
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)  # Position and render each cell


    # Figures out the exact screen position (in pixels) where a specific cell should be drawn
    # Tells that cell to draw itself at that position
    # Creates a brief animation pause so you can watch the maze being built
    def _draw_cell(self, i, j):
        # Safety check: if no window exists, don't try to draw anything
        if self._win is None:
            return
        # Calculate the position of each cell in the grid
        x1 = self._x1 + i * self._cell_size_x  # Left edge: maze origin x + (column number * cell width)
        y1 = self._y1 + j * self._cell_size_y  # Top edge: maze origin y + (row number * cell height)

        # Calculate the opposite corner by adding one cell's dimensions
        x2 = x1 + self._cell_size_x  # Right edge = left edge + cell width
        y2 = y1 + self._cell_size_y  # Bottom edge = top edge + cell height

        # Get the cell at position [i][j] and tell it to draw itself
        cell = self._cells[i][j]  # define our maze matrix
        cell.draw(x1, y1, x2, y2)  # draw the matrix

        # Animate the drawing process
        self._animate()

    # uses window's redraw() method
    # then time.sleep() to keep each frame visible to eye
    def _animate(self):
        # Safety check: if no window exists, don't try to draw anything
        if self._win is None:
            return
        self._win.redraw()  # redraw the window
        time.sleep(0.03)  # pause Xs between draw frames


    # always entrance topleft, exit bottom right
    # remove outerwall to each
    def _break_entrance_and_exit(self):
        enter_cell = self._cells[0][0]  # topleft has matrix index 0 for x & y
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]  # botright has matrix index #row/col - 1 (index starts @ 0)

        # Remove left wall from entrance and redraw the cell
        enter_cell.has_left_wall = False  # set entrance left wall to not draw
        self._draw_cell(0, 0)  # REDRAW the entrance cell

        # Remove right wall from exit and redraw the cell
        exit_cell.has_right_wall = False  # set exit right wall to not draw
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)  # REDRAW the exit cell

        # Animate the drawing process
        self._animate()


    # our DFS algorithm for breaking walls
    # i = column, j = row
    def _break_walls_r(self, i, j):
        # Mark the current cell as visited
        self._cells[i][j].visited = True

        # start an infinite loop
        while True:
            to_visit = []  # empty list of neighbours to visit

            # Get the neighbours
            # First we'll define traversal directions in the 2D-grid
            directions = [(-1, 0),    # Left
                            (1, 0),   # Right
                            (0, -1),  # Up
                            (0, 1)]   # Down
            
            # Defining each cell's position in direction to search
            for direction in directions:  # for each direction
                neighb_i = i + direction[0]  # neighbour column
                neighb_j = j + direction[1]  # neighbour row

                # Check if this neighbour is valid and unvisited
                if (neighb_i >= 0 and neighb_i < self._num_cols and   # check if in valid col number of maze
                    neighb_j >= 0 and neighb_j < self._num_rows and   # check if in valid row number of maze
                    not self._cells[neighb_i][neighb_j].visited):     # check if has been visited
                    to_visit.append((neighb_i, neighb_j))  # add to list if valid and not visited

            # If there are not available directions, draw the current cell and break out of loop
            if not to_visit:           # if list empty
                self._draw_cell(i, j)  # draw the current cell
                return                 # early return to exit the loop (Note: break would kill recursion...)
            
            # If there are available neighbours, randomly choose one
            target_cell_index = random.randrange(len(to_visit))  # choose random index from to_vist
            target_cell_coord = to_visit[target_cell_index]  # get the coordinates for that index value

            # Now need to break out the wall
            target_i = target_cell_coord[0]  # get target cell's col
            target_j = target_cell_coord[1]  # get target cell's row

            # Left neighbour break check
            if target_i == i - 1:  # if target is to left of current
                self._cells[i][j].has_left_wall = False  # remove current cell's left wall
                self._cells[target_i][target_j].has_right_wall = False  # remove target's right

            # Right neighbour break check
            if target_i == i + 1:  # if target is to right of current
                self._cells[i][j].has_right_wall = False  # remove current cell's right wall
                self._cells[target_i][target_j].has_left_wall = False  # remove target's left

            # Up neighbour break check
            if target_j == j - 1:  # if target is above current
                self._cells[i][j].has_top_wall = False  # remove current cell's top wall
                self._cells[target_i][target_j].has_bottom_wall = False  # remove target's bottom

            # Down neighbour break check
            if target_j == j + 1:  # if target is below current
                self._cells[i][j].has_bottom_wall = False  # remove current cell's bottom wall
                self._cells[target_i][target_j].has_top_wall = False  # remove target's top

            # Finally, move to target cell by recursively calling the method
            self._break_walls_r(target_i, target_j)


    # resets all cells visited flag to False -- allows running again when solving the maze
    def _reset_cells_visited(self):
        for col in self._cells:  # for each column in the maze's cells
            for cell in col:  # for each row (cell) in each column 
                cell.visited = False  # set it to not visited


    # calls the recursive solving method
    # returns True if solvable, False if not
    def _solve(self):
        if self._solve_r(0, 0):  # i=0, j=0
            return True  # it's solvable!
        return False  # it's unsolvable...


    # solving the maze method
    # Uses DFS as well
    # returns True if solvable, False if not
    def _solve_r(self, i, j):
        # Animate the drawing process
        self._animate()
        # Mark the current cell as visited
        self._cells[i][j].visited = True

        # BASE CASE OF RECURSION:
        # if you are at the exit cell, you're done!
        exit_i = self._num_cols - 1  # exit cell's col index
        exit_j = self._num_rows - 1  # exit cell's row index
        if i == exit_i and j == exit_j:  # if it matches both
            return True  # it's solvable!
        
        # Define all four possible directions to explore from current cell
        # Each direction is represented by a tuple containing:
        # 1. dx: Change in x-coordinate (-1=left, 1=right, 0=no change)
        # 2. dy: Change in y-coordinate (-1=up, 1=down, 0=no change)
        # 3. wall_check: A lambda function that checks if there's no wall in that direction
        # 4. next_cell: A lambda function that returns the cell in that direction
        directions = [
            # LEFT: move x-1, check left wall, get left cell
            (-1, 0, lambda x, y: not self._cells[x][y].has_left_wall, lambda x, y: self._cells[x-1][y]),
            # RIGHT: move x+1, check right wall, get right cell
            (1, 0, lambda x, y: not self._cells[x][y].has_right_wall, lambda x, y: self._cells[x+1][y]),
            # UP: move y-1, check top wall, get upper cell
            (0, -1, lambda x, y: not self._cells[x][y].has_top_wall, lambda x, y: self._cells[x][y-1]),
            # DOWN: move y+1, check bottom wall, get lower cell
            (0, 1, lambda x, y: not self._cells[x][y].has_bottom_wall, lambda x, y: self._cells[x][y+1])
        ]

        # Try each possible direction
        for dx, dy, wall_check, next_cell in directions:
            # Calculate the new coordinates of the cell in this direction
            new_i, new_j = i + dx, j + dy
            
            # Validate move: within bounds, no wall, and not yet visited
            if (0 <= new_i < self._num_cols and  # 1. The new x-coordinate is within the maze boundaries
                0 <= new_j < self._num_rows and  # 2. The new y-coordinate is within the maze boundaries
                wall_check(i, j) and             # 3. There is no wall blocking the path in this direction
                not next_cell(i, j).visited):    # 4. The cell in this direction hasn't been visited yet
                
                # Draw a visual representation of moving from current cell to next cell
                # This visualizes the path being explored
                self._cells[i][j].draw_move(next_cell(i, j))
                
                # Recursively attempt to solve the maze from this new position
                # If this path leads to the end, return True to propagate success up the call stack
                if self._solve_r(new_i, new_j):
                    return True
                
                # If we get here, this path didn't lead to a solution -- set undo=True
                # Backtrack: erase the move we just drew (by passing True as second parameter)
                # This visually represents abandoning this path
                self._cells[i][j].draw_move(next_cell(i, j), True)

        # BASE CASE OF FAILURE:
        # if no route works
        return False  # it's unsolvable...

# Sample trace through of this:
# When processing the LEFT direction:

# 1. Get the direction data
# dx, dy = -1, 0
# wall_check = lambda x, y: not self._cells[x][y].has_left_wall
# next_cell = lambda x, y: self._cells[x-1][y]

# 2. Calculate new position
# new_i = i + dx  # i - 1 (one cell to the left)
# new_j = j + dy  # j (same row)

# 3. Check if move is valid
# is_within_bounds = (0 <= new_i < self._num_cols and 0 <= new_j < self._num_rows)
# has_no_wall = wall_check(i, j)  # Checks if self._cells[i][j].has_left_wall is False
# is_not_visited = not next_cell(i, j).visited  # Checks if self._cells[i-1][j].visited is False

# 4. If valid, make the move
# if is_within_bounds and has_no_wall and is_not_visited:
#     # Draw the move and continue exploring
#     self._cells[i][j].draw_move(self._cells[i-1][j])
#     self._solve_r(new_i, new_j)  # Recursive call with new position

# Summary:
# Set up direction info: move left (-1, 0)
# Create two helper functions: one to check if there's no wall on our left, and another to get the cell on our left
# Calculate where we'd end up: one cell to the left, same row
# Check four things:
# Are we still inside the maze?
# Is there no wall blocking us?
# Has that cell not been visited before?
# If all checks pass, we draw a line showing our move and continue exploring from that new cell