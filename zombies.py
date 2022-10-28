import random
from turtle import Turtle


class Zombie(Turtle):
    def __init__(self):
        super().__init__()
        self.zombie_list = []

    def create_a_zombie(self):
        self.shape('circle')
        self.color('darkgreen')
        self.penup()
        self.goto(self.random_location_generator())
        zombie = [self, 5]
        self.zombie_list.append(zombie)
        print(f'self.zombieList: {len(self.zombie_list)}')
        return zombie


    def create_zombies(self):
        self.create_a_zombie()
        print(len(self.zombie_list))


    def move_zombies(self, user_tuple, move_speed):
        for zombie_tuple in self.zombie_list:
            zombie = zombie_tuple[0]
            user = user_tuple[0]
            new_heading = zombie.towards(user.xcor(), user.ycor())
            zombie.setheading(new_heading)
            zombie.speed(0)
            zombie.forward(move_speed)


    def random_location_generator(self):
        location = (random.randint(-400, 400), random.randint(-400, 400))
        return location
