import random
import turtle as t

tim = t.Turtle()

colors = ["MediumBlue", "ForestGreen", "MediumSpringGreen", "Brown", "Coral", "PeachPuff", "Chocolate", "GreenYellow",
          "LightCoral", "Gold", "Crimson", "Magenta", "BlueViolet"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

