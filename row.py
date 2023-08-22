from constans import SCREEN_WIDTH, BLOCK_SIZE
from grid import Grid


class Row:
    def __init__(self, y):
        self.y_cor = y
        self.grids = []
        self.create_row()

    def create_row(self):
        """Creates a new row on the grid at the rows y coordinate"""
        limit = int(SCREEN_WIDTH/2 - BLOCK_SIZE/2)
        for i in range(-limit, limit, BLOCK_SIZE):
            grid = Grid()
            grid.set_pos(x=i+ BLOCK_SIZE/2, y=self.y_cor)
            self.grids.append(grid)
        #print(len(self.grids))

    def is_grid_null(self, x):
        """Checks if the grid's block data is none, returns True if yes"""
        block = self.get_block(x)
        if block is None:
            return True
        return False

    def get_block(self, x):
        """Returns the block of the grid located at the specified x coordinate"""
        block = None
        for grid in self.grids:
            if grid.x_cor == x:
                block = grid.block
        return block

    def is_empty(self):
        """Check if the row is empty: every grids' block is none, return True if yes"""
        for grid in self.grids:
            if not grid.is_empty():
                return False
        return True

    def is_full(self):
        """Check if every grids' block has a value, return True if yes"""
        for grid in self.grids:
            if grid.block is None:
                return False
        return True

    def clear_row(self):
        """Clears every block in the row: hide the block then make it noe"""
        for grid in self.grids:
            grid.clear()

    def move_blocks(self):
        """Moves every block in the row to the row's y coordinate"""
        for grid in self.grids:
            if grid.block is not None:
                block = grid.block
                #print(f"Row y: {self.y_cor}; Block x: ")
                block.goto(x=block.xcor(), y=self.y_cor)
