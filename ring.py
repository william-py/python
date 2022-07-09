# python
import turtle as t
t.Screen().bgcolor("black")
t.pensize(2)
t.speed(10)

for i in range(6):
    for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
        t.color(color)
        t.circle(100)
        t.left(10)
    t.hideturtle()
t.done()
