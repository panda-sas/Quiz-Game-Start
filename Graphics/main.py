import random
from turtle import Turtle, Screen

timmy = Turtle()

# dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# draw shapes
colors = ["ForestGreen", "Aquamarine", "DarkOrange", "DarkOrchid", "Maroon", "Cyan", "Red", "Magenta", "Yellow",
          "LimeGreen", "PaleVioletRed"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
