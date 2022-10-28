from turtle import Turtle
FONT = ('Times', 20, 'bold')

writer = Turtle()
writer.penup()
writer.hideturtle()


def write_game_over():
    writer.penup()
    writer.color('black')
    writer.hideturtle()
    writer.goto(-150, 400)
    writer.write('---- Game Over ----', font=FONT)


def remove_game_over():
    writer.clear()
    # writer.reset()
