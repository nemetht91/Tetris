from block import Block


class Grid:
    def __init__(self):
        self.block: Block = None
        self.x_cor = 0
        self.y_cor = 0

    def set_pos(self,x, y):
        self.x_cor = x
        self.y_cor = y

    def get_block(self, block: Block):
        if self.block is None:
            self.block = block

    def clear(self):
        if self.block is not None:
            self.block.hideturtle()
            self.block = None

    def is_empty(self):
        if self.block is None:
            return True
        return False
