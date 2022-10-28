from turtle import Turtle


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.block_list = []
        self.hideturtle()
        self.BLOCK_COUNTER = 0
        self.block_color_value = 0


    def create_block(self, user_object, block_color, block_life_points):
        self.BLOCK_COUNTER += 1
        x = user_object.xcor()
        y = user_object.ycor()
        heading = user_object.heading()
        z = Block()
        z.shape('square')
        z.color(block_color)
        z.block_color_value = block_life_points
        z.penup()

        if heading == 0:
            z.goto(x + 20, y)
        elif heading == 90:
            z.goto(x, y + 20)
        elif heading == 180:
            z.goto(x - 20, y)
        elif heading == 270:
            z.goto(x, y - 20)
        z.showturtle()
        self.block_list.append([z, z.block_color_value])
        print(len(self.block_list))
        return self.block_list


    def delete_radius_of_blocks(self, user_object, distance_to_delete, other_list=None):
        print(f'a_block was here')
        print(len(self.block_list))
        man_list = []
        man_list.append(user_object)
        for the_user_object in range(len(self.block_list)):
            for block_tuple in self.block_list:
                print(f'a_block was here 2')
                if user_object[0].distance(block_tuple[0].xcor(), block_tuple[0].ycor()) < distance_to_delete:
                    block_tuple[0].goto(5000, 5000)
                    self.block_list.remove(block_tuple)
            if other_list is not None:
                for zombie_tuple in other_list:
                    zombie = zombie_tuple[0]
                    if user_object[0].distance(zombie.xcor(), zombie.ycor()) < distance_to_delete:
                        zombie.goto(5000, 5000)
                        other_list.remove(zombie_tuple)


    def remove_life_points(self, block_tuple):
        block_tuple[1] -= 1
        if block_tuple[1] == 0:
            block_tuple[0].goto(5000, 5000)
            self.block_list.remove(block_tuple)




