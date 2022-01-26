import time
import os

from geometric_primitives import utils as utils_gp

save_dir = os.path.join('../', "input")

def save_bricks(list_bricks: list, name: str):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    print('# Bricks: {}'.format(len(list_bricks)))

    for i, bricks in enumerate(list_bricks):
        print('Saving bricks {}'.format(i+1))
        utils_gp.save_bricks(bricks, save_dir, str_file=name + '_' + str(i+1))
        time.sleep(1)

if __name__ == '__main__':
    from geometric_primitives import bricks
    from geometric_primitives import brick

    bricks_ = bricks.Bricks(2)
    list_bricks = []

    for i in range(0, 2):
        brick_ = brick.Brick()
        brick_.set_position([0, 0, i])
        brick_.set_direction(i)
        list_bricks.append(brick_)

    for brick_ in list_bricks:
        bricks_.add(brick_)

    save_bricks([bricks_], 'save_bricks_example')