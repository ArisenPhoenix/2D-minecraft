from zombies import *
from blocks import *
import turtle
WINDOW_X = 1000
WINDOW_Y = 1000

'''------------------ Controlling Zombie Behavior ----------------------'''


def zombie_factory(object_to_use: Zombie, level_counter: int, zombie_life_points: int):
    for a_level in range(2*level_counter):
        zombie = Zombie()
        zombie.penup()
        zombie.speed(0)
        zombie.shape('circle')
        zombie.color('green')
        zombie.goto(random.randint(-400, 400), random.randint(-400, 400))
        object_to_use.zombie_list.append([zombie, zombie_life_points])
        print('This is in zombie factory')
    return object_to_use.zombie_list


def kill_zombie(zombie_tuple, list_of_zombies):
    zombie = zombie_tuple[0]
    # throw_away_list.append(zombie_tuple)
    zombie.goto(5000, 5000)
    list_of_zombies.remove(zombie_tuple)


def spawn_new_zombies(type_of_zombie, current_level, zombie_life_points):
    zombie_factory(type_of_zombie, current_level, zombie_life_points)

# TODO Figure Out How to Save Zombies to another list and reuse them so game doesn't slow down
    # def spawn_new_zombies(type_of_zombie, current_level, zombie_life_points, list_of_creatures, list_of_throw_aways):
    #     counter = 0
    #     for a_level in range(current_level):
    #         current_level -= 1
    #         if len(list_of_throw_aways) > 0:
    #             for a_creature in range(len(list_of_throw_aways*2)):
    #                 if len(list_of_throw_aways) > 0:
    #                     list_of_creatures.append(a_creature)
    #                 else:
    #                     zombie_factory(type_of_zombie, current_level, zombie_life_points)
    #                 if current_level == 0:
    #                     return


def remove_life_points(a_tuple, a_list):
    a_tuple[1] -= 1
    if a_tuple[1] == 0:
        kill_zombie(a_tuple, a_list)


def check_hit(list_of_arrows, list_of_zombies):
    counter = 0
    for arrow in list_of_arrows:
        for zombie_tuple in list_of_zombies:
            zombie = zombie_tuple[0]

            if arrow.distance(zombie.xcor(), zombie.ycor()) < 10:
                zombie.setheading(zombie.heading() - 180)
                zombie.forward(5)
                list_of_arrows.remove(arrow)
                arrow.goto(5000, 5000)
                counter += 1
                zombie_tuple[1] -= 1
                print(f'zombie life: {zombie_tuple[1]}')
                if zombie_tuple[1] == 0:
                    kill_zombie(zombie_tuple, list_of_zombies)

                print(len(list_of_zombies))
    if counter > 0:
        return True



'''------------------ Controlling User Behavior ----------------------'''


def man_shoots(user_tuple, list_of_arrows):
    an_arrow = turtle.Turtle()
    an_arrow.penup()
    an_arrow.color('black')
    an_arrow.goto(user_tuple[0].xcor(), user_tuple[0].ycor())
    an_arrow.setheading(user_tuple[0].heading())
    an_arrow.forward(5)
    list_of_arrows.append(an_arrow)


def border(user_tuple, length=1000, width=1000):
    x = .95*(length/2)
    y = .95*(width/2)
    user = user_tuple
    if user.xcor() > x:
        user.goto(x, user.ycor())
    elif user.xcor() < -x:
        user.goto(-x, user.ycor())
    elif user.ycor() > y:
        user.goto(user.xcor(), y)
    elif user.ycor() < -y:
        user.goto(user.xcor(), -y)



'''------------------ Controlling Block Behavior ----------------------'''


def block_factory(object_to_use: Block, block_value):
    block = Block()
    block.penup()
    block.speed(0)
    block.shape('circle')
    block.color('green')
    block.goto(random.randint(-400, 400), random.randint(-400, 400))
    object_to_use.block_list[block] = block_value
    print(len(object_to_use.block_list))
    print('This is in block factory')
    return object_to_use.block_list


# def set_block_down(user_tuple, list_of_blocks: Block().block_list, block_color):
#     LAST_BLOCK_USED = block_color
#     x = user_tuple[0].xcor()
#     y = user_tuple[0].ycor()
#     heading = user_tuple[0].heading()
#     block = turtle.Turtle()
#     block.shape('square')
#     block.color(block_color)
#     block.hideturtle()
#     block.penup()
#     if heading == 0:
#         block.goto(x + 20, y)
#     elif heading == 90:
#         block.goto(x, y + 20)
#     elif heading == 180:
#         block.goto(x - 20, y)
#     elif heading == 270:
#         block.goto(x, y - 20)
#     block.showturtle()
#     list_of_blocks.append(block)
#     return LAST_BLOCK_USED


def create_filler():
    filler = turtle.Turtle()
    filler.color('green')
    filler.penup()
    filler.pensize(20)
    filler.pencolor('green')
    filler.shape('square')
    filler.hideturtle()
    return filler


def delete_block(user_tuple, list_of_blocks):
    user = user_tuple[0]
    heading = user.heading()

    for block_tuple in list_of_blocks:
        print('trying to delete a block')
        # print(block_tuple[1])
        block = block_tuple[0]
        block_X_cor = block.xcor()
        block_Y_cor = block.ycor()

        distance = 10

        if heading == 0:
            if block_X_cor >= user.xcor()+distance \
                    and user.distance(block_X_cor, block_Y_cor) < 25:
                block.goto(5000, 5000)
                list_of_blocks.remove(block_tuple)

        elif heading == 90:
            if block_Y_cor >= user.ycor()+distance \
                    and user.distance(block_X_cor, block_Y_cor) < 25:
                block.goto(5000, 5000)
                list_of_blocks.remove(block_tuple)

        elif heading == 180:
            if block_X_cor <= user.xcor()-distance \
                    and user.distance(block_X_cor, block_Y_cor) < 25:
                block.goto(5000, 5000)
                list_of_blocks.remove(block_tuple)

        elif heading == 270:
            if block_Y_cor <= user.ycor()-distance \
                    and user.distance(block_X_cor, block_Y_cor) < 25:
                block.goto(5000, 5000)
                list_of_blocks.remove(block_tuple)


def delete_large_radius_of_blocks(user_object, list_of_blocks):
    for a_block in list_of_blocks:
        if user_object[0].distance(a_block.xcor(), a_block.ycor()) < 55:
            a_block.goto(5000, 5000)


def area_fill(filling_turtle, coordinates_1, coordinates_2, color: str):
    filling_turtle.penup()
    if coordinates_1[1] > coordinates_2[1]:
        Coors1 = coordinates_1
        Coors2 = coordinates_2
    else:
        Coors1 = coordinates_2
        Coors2 = coordinates_1
    filling_turtle.goto(Coors1)
    filling_turtle.color(color)
    print(f'Coords1: {Coors1}')
    print(f'Coords2: {Coors2}')
    while filling_turtle.ycor() > Coors2[1]:
        filling_turtle.pendown()
        filling_turtle.setheading(0)
        filling_turtle.forward(20)
        filling_turtle.goto(Coors2[0], filling_turtle.ycor())
        filling_turtle.setheading(270)
        filling_turtle.forward(20)
        filling_turtle.goto(Coors1[0], filling_turtle.ycor())
        filling_turtle.setheading(270)
        filling_turtle.forward(20)
        filling_turtle.goto(Coors2[0], filling_turtle.ycor())


def options(window_object, filling_turtle, click_coords_1, click_coords_2, last_color_used):
    an_input = window_object.textinput(title='More Actions', prompt='What would you like to do? A for Area Fill etc.')
    window_object.listen()
    if an_input == 'F':
        area_fill(filling_turtle, click_coords_1, click_coords_2, last_color_used)
        print('F has been executed')
        return last_color_used
    elif an_input == 'e':
        print('e has been executed')
        return False
    return True



def screen_setup(user_object):
    player = user_object[0]
    player.pendown()
    player.pencolor('beige')
    player.speed(0)
    player.setheading(0)
    player.forward(1500)
    player.setheading(270)
    player.forward(20)
    player.setheading(180)
    player.forward(1500)
    player.setheading(270)
    player.forward(20)
    player.setheading(0)




'''------------------ Controlling Arrow Behavior ----------------------'''


def move_arrows(list_of_arrows):
    for arrow in list_of_arrows:
        arrow.forward(5)


def remove_arrows(list_of_arrows):
    for arrow in list_of_arrows:
        if arrow.xcor() > WINDOW_X:
            list_of_arrows.remove(arrow)
        elif arrow.xcor() < -WINDOW_X:
            list_of_arrows.remove(arrow)
        elif arrow.ycor() > WINDOW_Y:
            list_of_arrows.remove(arrow)
        elif arrow.ycor() < -WINDOW_Y:
            list_of_arrows.remove(arrow)


'''------------------ Controlling Game Behavior ----------------------'''


def zombie_colliding_with_blocks(list_of_zombies, list_of_blocks, block_num):
    for zombie in list_of_zombies:
        for block in list_of_blocks:
            if block.distance(zombie.xcor(), zombie.ycor()) < 20:

                block_num -= 1
                if block_num == 0:
                    block.goto(5000, 5000)
                    list_of_zombies.remove(block)
