import random

from block import Block
from constans import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, SCREEN_MARGIN
from row import Row

class Shape:
    def __init__(self):
        self.blocks = [Block(), Block(), Block(), Block()]
        self.position = [0, 0]
        self.orientations = [0, 90, 180, 270]
        self.orientation = 0
        self.dont_move_down = False
        self.user_action_active = False

    def get_random_orientation(self):
        self.orientation = random.choice(self.orientations)

    def draw_shape(self):
        self.user_action_active = False

    def rotate(self):
        if self.can_rotate():
            index = self.orientations.index(self.orientation)
            if index >= len(self.orientations) - 1:
                index = 0
            else:
                index += 1
            self.orientation = self.orientations[index]

    def move(self, x_dir, y_dir):
        self.position[0] += x_dir
        self.position[1] += y_dir

    def enable_move_down(self):
        self.dont_move_down = False

    def move_down(self):
        if not self.dont_move_down:
            self.move(x_dir=0, y_dir=-BLOCK_SIZE)
        self.dont_move_down = False

    def move_left(self):
        if self.can_move_left():
            self.user_action_active = True
            self.dont_move_down = True
            self.move(x_dir=-BLOCK_SIZE, y_dir=0)
            self.draw_shape()

    def move_right(self):
        if self.can_move_right():
            self.user_action_active = True
            self.dont_move_down = True
            self.move(x_dir=BLOCK_SIZE, y_dir=0)
            self.draw_shape()

    def can_move_left(self):
        if self.user_action_active:
            return False
        for block in self.blocks:
            if block.xcor() <= - (SCREEN_WIDTH/2 - 1.5*BLOCK_SIZE):
                return False
        return True

    def can_move_right(self):
        if self.user_action_active:
            return False
        for block in self.blocks:
            if block.xcor() >= (SCREEN_WIDTH/2 - 1.5*BLOCK_SIZE):
                return False
        return True

    def can_move_down(self):
        for block in self.blocks:
            if block.ycor() <= -(SCREEN_HEIGHT/2 - BLOCK_SIZE):
                return False
        return True

    def can_rotate(self):
        if self.orientation == 90 or self.orientation == 270:
            if self.position[0] >= SCREEN_WIDTH / 2 - 2 * BLOCK_SIZE:
                return False
        if self.orientation == 0 or self.orientation == 180:
            if self.position[1] <= - SCREEN_HEIGHT / 2 + 3 * BLOCK_SIZE:
                return False
        return True


class ShapeO(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        self.blocks[0].goto(x=self.position[0], y=self.position[1])
        self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
        self.blocks[2].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
        self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        super().draw_shape()

    def can_rotate(self):
        return True


class ShapeI(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0 or self.orientation == 180:
            x_offs = BLOCK_SIZE
            y_offs = 0
        else:
            x_offs = 0
            y_offs = -BLOCK_SIZE
        for block in self.blocks:
            index = self.blocks.index(block)
            block.goto(x=self.position[0] + index*x_offs, y=self.position[1] + index*y_offs)
        super().draw_shape()

    def can_rotate(self):
        if self.orientation == 90 or self.orientation == 270:
            if self.position[0] >= SCREEN_WIDTH / 2 - 3*BLOCK_SIZE:
                return False
        if self.orientation == 0 or self.orientation == 180:
            if self.position[1] <= -SCREEN_WIDTH/2 + 3*BLOCK_SIZE:
                return False
        return True


class ShapeT(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1])
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        elif self.orientation == 90:
            self.blocks[0].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1]-BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - 2 * BLOCK_SIZE)
        elif self.orientation == 180:
            self.blocks[0].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1]-BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + 2 * BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        else:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0], y=self.position[1] - 2 * BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        super().draw_shape()


class ShapeL(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1])
            self.blocks[3].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
        elif self.orientation == 90:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - 2 * BLOCK_SIZE)
        elif self.orientation == 180:
            self.blocks[0].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1]-BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + 2 * BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        else:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0], y=self.position[1] - 2 * BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1]- 2 * BLOCK_SIZE)
        super().draw_shape()


class ShapeJ(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1])
            self.blocks[3].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        elif self.orientation == 90:
            self.blocks[0].goto(x=self.position[0], y=self.position[1] - 2*BLOCK_SIZE)
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - 2 * BLOCK_SIZE)
        elif self.orientation == 180:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1]-BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + 2 * BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        else:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0], y=self.position[1] - 2 * BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
        super().draw_shape()


class ShapeZ(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0 or self.orientation == 180:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + 2*BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
        else:
            self.blocks[0].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0], y=self.position[1] - 2 * BLOCK_SIZE)
        super().draw_shape()


class ShapeS(Shape):
    def __init__(self):
        super().__init__()

    def draw_shape(self):
        if self.orientation == 0 or self.orientation == 180:
            self.blocks[0].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1])
            self.blocks[1].goto(x=self.position[0] + 2 * BLOCK_SIZE, y=self.position[1])
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
        else:
            self.blocks[0].goto(x=self.position[0], y=self.position[1])
            self.blocks[1].goto(x=self.position[0], y=self.position[1] - BLOCK_SIZE)
            self.blocks[2].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - BLOCK_SIZE)
            self.blocks[3].goto(x=self.position[0] + BLOCK_SIZE, y=self.position[1] - 2 * BLOCK_SIZE)
        super().draw_shape()
