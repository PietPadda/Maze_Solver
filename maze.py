# MAZE.PY
from cell import Cell  # import the Cell class
import time  # for time.sleep()

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
        ):
        self._cells = []  # initiate cell list to be filled
        self._x1 = x1  # x coord of topleft of maze
        self._y1 = y1  # y coord of topleft of maze
        self._num_rows = num_rows  # no of rows in maze
        self._num_cols = num_cols  # no of cols in maze
        self._cell_size_x = cell_size_x  # width of each cell in pixels
        self._cell_size_y = cell_size_y  # height of each cell in pixels
        self._win = win  # window objt where maze is drawn

        self._create_cells()  # calls the cell creation method
        self._break_entrance_and_exit()  # create enter/exit cells

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
