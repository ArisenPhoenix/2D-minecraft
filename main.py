import time
from functions import *
from zombies import *
from blocks import *
from screen_writer import *
arrow_list = []
counter = 0
Fill_COORS1 = (0, 0)
Fill_COORS2 = (0, 0)
going = True
window = turtle.Screen()
window.tracer(0)
WINDOW_X = WINDOW_X
WINDOW_Y = WINDOW_Y
window.screensize(WINDOW_X, WINDOW_Y)
window.setup(width=WINDOW_X, height=WINDOW_Y)
window.title('BlockMan')

generic_zombie_health = 5
LEVEL = 0
USER_SIZE = 1
ZOMBIE_SPEED = .5
filler = create_filler()


def create_man():
    man = turtle.Turtle()
    man.shape('turtle')
    man.shapesize(USER_SIZE)
    man.color('blue')
    man.penup()
    man.goto(-750, 500)
    man = [man, 100]
    return man


generic_zombie = Zombie()
generic_zombie.create_a_zombie()
zombie_list = zombie_factory(generic_zombie, LEVEL, 2)
BLOCK_COUNTER = 0

a_list = []
generic_block = Block()
BLOCK_LIST = generic_block.block_list
LAST_BLOCK_USED = ''
BLACK_COUNTER = 0
GOLD_COUNTER = 0
RUBY_COUNTER = 0
SAPPHIRE_COUNTER = 0
EMERALD_COUNTER = 0
OBSIDIAN_COUNTER = 0
PINK_COUNTER = 0
QUARTZ_COUNTER = 0
GENERIC_ZOMBIE_TRASH = []
GENERIC_BLOCK_TRASH = []
GENERIC_ARROW_TRASH = []
man_info = create_man()


def reset_block_counters():
    global BLACK_COUNTER, GOLD_COUNTER, RUBY_COUNTER, SAPPHIRE_COUNTER, EMERALD_COUNTER, OBSIDIAN_COUNTER, PINK_COUNTER, QUARTZ_COUNTER
    BLACK_COUNTER = 0
    GOLD_COUNTER = 0
    RUBY_COUNTER = 0
    SAPPHIRE_COUNTER = 0
    EMERALD_COUNTER = 0
    OBSIDIAN_COUNTER = 0
    PINK_COUNTER = 0
    QUARTZ_COUNTER = 0


def check_arrow_hit(list_of_arrows, list_of_zombies):
    counter = 0
    for arrow in list_of_arrows:
        for zombie_tuple in list_of_zombies:
            zombie = zombie_tuple[0]
            if arrow.distance(zombie.xcor(), zombie.ycor()) < 21:
                counter += 1
                kill_zombie(zombie_tuple, list_of_zombies)
    if counter > 0:
        return True


def reset_filler():
    filler.clear()
    filler.hideturtle()


def move_forward():
    if man_info[0].heading() != 90:
        man_info[0].setheading(90)
    else:
        man_info[0].forward(20)


def move_backward():
    if man_info[0].heading() != 270:
        man_info[0].setheading(270)
    else:
        man_info[0].forward(20)


def move_left():
    if man_info[0].heading() != 180:
        man_info[0].setheading(180)
    else:
        man_info[0].forward(20)


def move_right():
    if man_info[0].heading() != 0:
        man_info[0].setheading(0)
    else:
        man_info[0].forward(20)


def delete_a_block():
    delete_block(man_info, BLOCK_LIST)


def big_boom():
    generic_block.delete_radius_of_blocks(man_info, 100)


def little_boom():
    generic_block.delete_radius_of_blocks(man_info, 50)


def set_gold_down():
    global LAST_BLOCK_USED, BLOCK_LIST, GOLD_COUNTER
    GOLD_COUNTER += 1
    if GOLD_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='gold', block_life_points=5)
    LAST_BLOCK_USED = 'gold'
    return LAST_BLOCK_USED


def set_emerald_down():
    global LAST_BLOCK_USED, BLOCK_LIST, man_info, EMERALD_COUNTER
    EMERALD_COUNTER += 1
    if EMERALD_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='green', block_life_points=5)
    LAST_BLOCK_USED = 'green'
    return LAST_BLOCK_USED


def set_ruby_down():
    global LAST_BLOCK_USED, BLOCK_LIST, RUBY_COUNTER
    RUBY_COUNTER += 1
    if RUBY_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='red', block_life_points=5)
    LAST_BLOCK_USED = 'red'
    return LAST_BLOCK_USED


def set_sapphire_down():
    global LAST_BLOCK_USED, BLOCK_LIST, SAPPHIRE_COUNTER
    SAPPHIRE_COUNTER += 1
    if SAPPHIRE_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='blue', block_life_points=5)
    LAST_BLOCK_USED = 'blue'
    return LAST_BLOCK_USED


def set_obsidian_down():
    global LAST_BLOCK_USED, BLOCK_LIST, OBSIDIAN_COUNTER
    OBSIDIAN_COUNTER += 1
    if OBSIDIAN_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='black', block_life_points=5)
    LAST_BLOCK_USED = 'black'
    return LAST_BLOCK_USED


def set_quartz_down():
    global LAST_BLOCK_USED, BLOCK_LIST, QUARTZ_COUNTER
    QUARTZ_COUNTER += 1
    if QUARTZ_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='white', block_life_points=5)
    LAST_BLOCK_USED = 'white'
    return LAST_BLOCK_USED


def set_pink_flower_down():
    global LAST_BLOCK_USED, BLOCK_LIST, PINK_COUNTER
    PINK_COUNTER += 1
    if PINK_COUNTER < 10:
        BLOCK_LIST = generic_block.create_block(user_object=man_info[0], block_color='pink', block_life_points=5)
    LAST_BLOCK_USED = 'pink'
    return LAST_BLOCK_USED


def on_click(x, y):
    global counter, Fill_COORS1, Fill_COORS2
    counter += 1
    print(x, y)
    if counter == 1:
        Fill_COORS1 = (x, y)
    elif counter == 2:
        Fill_COORS2 = (x, y)
        counter = 0


def open_options(x, y):
    global going
    Last_COLOR = options(window, filler, Fill_COORS1, Fill_COORS2, LAST_BLOCK_USED)
    if type(Last_COLOR) == type(bool):
        going = True


def shoot():
    man_shoots(man_info, arrow_list)


while man_info[0].xcor() <= 740 and man_info[0].ycor() >= -490:
    screen_setup(man_info)
    if man_info[0].ycor() <= -600 and man_info[0].xcor() >= 800:
        break
man_info[0].penup()
man_info[0].goto(0, 10)
window.listen()
window.onscreenclick(on_click, btn=1)
window.onscreenclick(open_options, btn=3)
window.onkeypress(move_forward, 'Up')
window.onkeypress(move_backward, 'Down')
window.onkeypress(move_left, 'Left')
window.onkeypress(move_right, 'Right')
window.onkeypress(set_gold_down, 'g')
window.onkeypress(set_emerald_down, 'e')
window.onkeypress(set_ruby_down, 'r')
window.onkeypress(set_sapphire_down, 's')
window.onkeypress(set_obsidian_down, 'b')
window.onkeypress(set_quartz_down, 'w')
window.onkeypress(set_pink_flower_down, 'p')
window.onkeypress(delete_a_block, 'd')
window.onkeypress(little_boom, 'q')
window.onkeypress(big_boom, 'Q')
window.onkeypress(open_options, 'O')
window.onkeypress(reset_filler, 'C')
window.onkeypress(shoot, 'space')


def check_zombie_block_collision(list_of_zombies, list_of_blocks):
    collision_counter = 0
    for zombie_tuple in list_of_zombies:
        zombie = zombie_tuple[0]
        for block_tuple in list_of_blocks:
            block = block_tuple[0]
            if zombie.distance(block.xcor(), block.ycor()) < 21:
                collision_counter += 1
                generic_block.remove_life_points(block_tuple)
                remove_life_points(zombie_tuple, zombie_list)
                remove_life_points(block_tuple, list_of_blocks)
                zombie.setheading(360 - zombie.heading()+180)
                zombie.back(5)
    if collision_counter > 0:
        return True


def check_user_dead(user_tuple: [Turtle, int], list_of_zombies):
    global going
    list_of_man = []
    list_of_man.append(user_tuple)
    for man in list_of_man:
        for zombie in list_of_zombies:
            if man[0].distance(zombie[0].xcor(), zombie[0].ycor()) < 14:
                print('zombie bite!!!')
                man[0].backward(20)
                remove_life_points(user_tuple, list_of_man)
                if man[1] == 0:
                    print('man dead')
                    write_game_over()
                    time.sleep(1)
                    remove_game_over()
                    man[1] = 5


def no_move_through_walls(user_tuple, list_of_blocks):
    list_of_man = []
    list_of_man.append(user_tuple)
    for man in list_of_man:
        for block in list_of_blocks:
            if man[0].distance(block[0].xcor(), block[0].ycor()) < 20:
                return True

while going:
    xcor = man_info[0].xcor()
    ycor = man_info[0].ycor()
    time.sleep(.01)
    window.update()
    if no_move_through_walls(man_info, BLOCK_LIST):
        man_info[0].backward(5)
    border(man_info[0], WINDOW_X, WINDOW_Y)
    move_arrows(arrow_list)
    check_user_dead(man_info, zombie_list)
    if check_hit(arrow_list, zombie_list):
        if len(zombie_list) == 0:
            LEVEL += 1
            reset_block_counters()
            spawn_new_zombies(generic_zombie, LEVEL, zombie_life_points=generic_zombie_health)
    if check_zombie_block_collision(zombie_list, BLOCK_LIST):
        if len(zombie_list) == 0:
            LEVEL += 1
            reset_block_counters()
            spawn_new_zombies(generic_zombie, LEVEL, zombie_life_points=generic_zombie_health)
    generic_zombie.move_zombies(user_tuple=man_info, move_speed=ZOMBIE_SPEED)


window.listen()
