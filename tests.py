import unittest  # Import the unittest framework for testing
from maze import Maze  # Import the Maze class from your maze module

class Tests(unittest.TestCase):  # Create a test class that inherits from unittest.TestCase
    # Define a test method to check cell creation
    def test_maze_create_cells(self):  
        num_cols = 12  # Set number of columns for the test maze
        num_rows = 10  # Set number of rows for the test maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)  # Create a maze with specified dimensions, explicitly setting win to None
        self.assertEqual(
            len(m1._cells),  # Get the number of column arrays in the maze
            num_cols,  # Should match the number of columns we specified
        )
        self.assertEqual(
            len(m1._cells[0]),  # Get the number of cells in the first column
            num_rows,  # Should match the number of rows we specified
        )


    # Define a test method to check cell creation - 5 row, 15 col
    def test_maze_create_cells_1to3(self):  
        num_cols = 5  # Set number of columns for the test maze
        num_rows = 15  # Set number of rows for the test maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)  # Create a maze with specified dimensions, explicitly setting win to None
        self.assertEqual(
            len(m1._cells),  # Get the number of column arrays in the maze
            num_cols,  # Should match the number of columns we specified
        )
        self.assertEqual(
            len(m1._cells[0]),  # Get the number of cells in the first column
            num_rows,  # Should match the number of rows we specified
        )


    # Define a test method to check cell creation - 1 row, 1 col
    def test_maze_create_cells_one_cell(self):  
        num_cols = 1  # Set number of columns for the test maze
        num_rows = 1  # Set number of rows for the test maze
        m1 = Maze(20, 20, num_rows, num_cols, 40, 40, win=None)  # Create a maze with specified dimensions, explicitly setting win to None
        self.assertEqual(
            len(m1._cells),  # Get the number of column arrays in the maze
            num_cols,  # Should match the number of columns we specified
        )
        self.assertEqual(
            len(m1._cells[0]),  # Get the number of cells in the first column
            num_rows,  # Should match the number of rows we specified
        )


    # Define a test method to check cell creation - 100 row, 100 col
    def test_maze_create_cells_massive(self):  
        num_cols = 100  # Set number of columns for the test maze
        num_rows = 100  # Set number of rows for the test maze
        m1 = Maze(50, 50, num_rows, num_cols, 4, 4, win=None)  # Create a maze with specified dimensions, explicitly setting win to None
        self.assertEqual(
            len(m1._cells),  # Get the number of column arrays in the maze
            num_cols,  # Should match the number of columns we specified
        )
        self.assertEqual(
            len(m1._cells[0]),  # Get the number of cells in the first column
            num_rows,  # Should match the number of rows we specified
        )


    # Define a test method to check cell creation - 1 row, 200 col
    def test_maze_create_cells_flat_row(self):  
        num_cols = 1  # Set number of columns for the test maze
        num_rows = 200  # Set number of rows for the test maze
        m1 = Maze(-50, -50, num_rows, num_cols, 200, 200, win=None)  # Create a maze with specified dimensions, explicitly setting win to None
        self.assertEqual(
            len(m1._cells),  # Get the number of column arrays in the maze
            num_cols,  # Should match the number of columns we specified
        )
        self.assertEqual(
            len(m1._cells[0]),  # Get the number of cells in the first column
            num_rows,  # Should match the number of rows we specified
        )


if __name__ == "__main__":  # This block only runs when the script is executed directly
    unittest.main()  # Run all the test methods in this file