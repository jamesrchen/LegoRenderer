from geometric_primitives import bricks
from geometric_primitives import brick

from save_bricks import save_bricks

bricks_ = bricks.Bricks(4)

brick_ = brick.Brick()
brick_.set_position([0, 0, 0])
brick_.set_direction(0)

bricks_.add(brick_)

save_bricks([bricks_], 'bricks')