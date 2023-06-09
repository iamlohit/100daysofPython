import turtle as t
import random

tim = t.Turtle()
s = t.Screen()
canvas = t.screensize(10, 10)
t.colormode(255)


def draw_shape():
    tim.speed(0)
    tim.pensize(15)
    tim.fd(30)
    angles = [90, 180, 270]
    angle = random.choice(angles)
    tim.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_circle():
    t.speed(0)
    t.pensize(2)
    t.circle(200)


for i in range(0, 360, 1):
    t.seth(i)
    draw_circle()
    t.pencolor(random_color())

s.exitonclick()

