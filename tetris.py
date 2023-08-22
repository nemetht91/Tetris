import random
import time
from turtle import Screen, Turtle

from constans import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, SCREEN_MARGIN, REFRESH_RATE
from row import Row
from shapes import Shape, ShapeZ, ShapeJ, ShapeI, ShapeL, ShapeT, ShapeO, ShapeS


class Tetris:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH + SCREEN_MARGIN, height=SCREEN_HEIGHT+SCREEN_MARGIN)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.current_shape: Shape = None
        self.shapes = [ShapeZ, ShapeJ, ShapeI, ShapeL, ShapeT, ShapeO, ShapeS]
        self.grid = Turtle()
        self.grid.hideturtle()
        self.grid.penup()
        self.grid.color("white")
        self.refresh_rate = REFRESH_RATE
        self.rows = []
        self.create_rows()
        self.game_over = False

    def check_row_full(self):
        """Check each row if it's full. If yes, clear every block then shifts every row's blocks by one row down"""
        for row in self.rows:
            while row.is_full():
                row.clear_row()
                self.shift_rows(self.rows.index(row))

    def shift_rows(self, index):
        """Shifts every row's block by one row down starting at the specified index"""
        for row_i in range(index, len(self.rows)):
            if row_i < len(self.rows) - 1:
                current_row = self.rows[row_i]
                next_row = self.rows[row_i + 1]
                for i in range(len(next_row.grids)):
                    if next_row.grids[i] is not None:
                        current_row.grids[i].block = next_row.grids[i].block
                        next_row.grids[i].block = None
                        #print(current_row.grids[i].block)
                        #print(next_row.grids[i].block)
                current_row.move_blocks()

    def add_shape_to_grid(self, shape: Shape):
        """Adds the current shape's block objects to the grid."""
        for row in self.rows:
            for grid in row.grids:
                for block in shape.blocks:
                    if grid.x_cor == block.xcor() and grid.y_cor == block.ycor():
                        grid.block = block
                        #print(f"{grid.x_cor}: {block.xcor()}; {grid.y_cor}: {block.ycor()}")
                        #print(f"Row: {self.rows.index(row)}; Grid: {grid.block}; Block: {block} ")

    def print_row_0(self):
        row = self.rows[0]
        for grid in row.grids:
            print(grid.block)

    def can_shape_move_down(self):
        """Checks if the grid is empty below the shape"""
        for block in self.current_shape.blocks:
            block_x = block.xcor()
            block_y = block.ycor() - BLOCK_SIZE
            row = self.get_row(y=block_y)
            if row is None:
                return True
            if not row.is_grid_null(x=block_x):
                #print(f"Row: {self.rows.index(row)} is not empty")
                return False
        return True

    def create_rows(self):
        """Create every row for the grid"""
        limit = int((SCREEN_HEIGHT-BLOCK_SIZE)/2)
        for i in range(-limit, limit, BLOCK_SIZE):
            row = Row(y=i)
            self.rows.append(row)

    def get_row(self, y):
        """Returns the row at the specified y coordinate"""
        for row in self.rows:
            if row.y_cor == y:
                return row

    def speed_up(self):
        """Sets the refresh rate to make the blocks move faster down"""
        self.refresh_rate = REFRESH_RATE / 4

    def speed_down(self):
        """Sets refresh rate back to normal"""
        self.refresh_rate = REFRESH_RATE

    def draw_frame(self):
        grid = self.grid
        grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=SCREEN_HEIGHT / 2)
        grid.pendown()
        grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=-SCREEN_HEIGHT / 2)
        grid.penup()
        grid.goto(x=(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=SCREEN_HEIGHT / 2)
        grid.pendown()
        grid.goto(x=(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=-SCREEN_HEIGHT / 2)
        grid.penup()
        grid.goto(x=(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=SCREEN_HEIGHT / 2)
        grid.pendown()
        grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=SCREEN_HEIGHT / 2)
        grid.penup()
        grid.goto(x=(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=-SCREEN_HEIGHT / 2)
        grid.pendown()
        grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=-SCREEN_HEIGHT / 2)
        grid.penup()

    def draw_grid(self):
        """Draws the grid"""
        grid = self.grid
        grid.goto(x= -(SCREEN_WIDTH/2 - BLOCK_SIZE/2), y=SCREEN_HEIGHT/2)
        grid_num = int(SCREEN_WIDTH/2*BLOCK_SIZE)
        for i in range(grid_num):
            grid.pendown()
            grid.goto(x=grid.xcor(), y= - SCREEN_HEIGHT/2)
            grid.penup()
            grid.goto(x=grid.xcor()+BLOCK_SIZE, y=SCREEN_HEIGHT/2)

        grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=SCREEN_HEIGHT / 2)
        grid_num = int(SCREEN_WIDTH / 2 * BLOCK_SIZE)
        for i in range(grid_num):
            grid.pendown()
            grid.goto(x=SCREEN_WIDTH / 2 - BLOCK_SIZE / 2, y=grid.ycor())
            grid.penup()
            grid.goto(x=-(SCREEN_WIDTH / 2 - BLOCK_SIZE / 2), y=grid.ycor() - BLOCK_SIZE)

    def get_new_shape(self):
        """Add a new random shape to the current_shape object"""
        shape = random.choice(self.shapes)
        self.current_shape = shape()
        self.current_shape.position = [0, SCREEN_HEIGHT / 2 + BLOCK_SIZE/2]
        self.current_shape.get_random_orientation()
        self.current_shape.draw_shape()
        self.init_controls()

    def is_collision_on_grid(self):
        for block in self.current_shape.blocks:
            block_x = block.xcor()
            block_y = block.ycor()
            row = self.get_row(block_y)
            if row is not None:
                grid_block = row.get_block(block_x)
                if grid_block is not None:
                    return True
        return False

    def move_left(self):
        self.current_shape.move_left()
        # Check if shape in the new position is colliding with a block on the grid
        if self.is_collision_on_grid():
            # Moving back to original pos
            self.current_shape.user_action_active = False
            self.current_shape.move_right()

    def move_right(self):
        self.current_shape.move_right()
        # Check if shape in the new position is colliding with a block on the grid
        if self.is_collision_on_grid():
            # Moving back to original pos
            self.current_shape.user_action_active = False
            self.current_shape.move_left()

    def rotate(self):
        old_orientation = self.current_shape.orientation
        self.current_shape.rotate()
        # Check if shape in new orientation is colliding with block already on the grid
        if self.is_collision_on_grid():
            # changing back orientation
            self.current_shape.user_action_active = False
            self.current_shape.orientation = old_orientation

    def init_controls(self):
        """Sets controls for moving and rotating the shapes"""
        self.screen.listen()
        self.screen.onkeypress(key="Left", fun=self.move_left)
        self.screen.onkeypress(key="Right", fun=self.move_right)
        self.screen.onkeyrelease(key="Left", fun=self.current_shape.enable_move_down)
        self.screen.onkeyrelease(key="Right", fun=self.current_shape.enable_move_down)
        self.screen.onkey(key="Up", fun=self.rotate)
        self.screen.onkeypress(key="Down", fun=self.speed_up)
        self.screen.onkeyrelease(key="Down", fun=self.speed_down)

    def check_game_over(self):
        """Game is over if the shape can't move down from the top row"""
        for block in self.current_shape.blocks:
            if block.ycor() >= SCREEN_HEIGHT/2 - BLOCK_SIZE:
                self.game_over = True

    def tetris(self):
        #self.draw_grid()
        self.draw_frame()
        #self.get_new_shape()
        while not self.game_over:
            self.get_new_shape()
            self.init_controls()
            while self.current_shape.can_move_down() and self.can_shape_move_down():
                self.current_shape.move_down()
                self.current_shape.draw_shape()
                self.screen.update()
                time.sleep(self.refresh_rate)
            self.add_shape_to_grid(self.current_shape)
            self.check_row_full()
            #self.print_row_0()
            self.check_game_over()
            self.screen.update()
            time.sleep(self.refresh_rate)
        self.screen.exitonclick()
