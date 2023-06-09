import turtle as t

tim = t.Turtle()
screen = t.Screen()


def w():
    tim.fd(20)


def s():
    tim.bk(20)


def a():
    tim.lt(90)
    tim.fd(20)


def d():
    tim.rt(90)
    tim.fd(20)
Hi TeahffrI thinki thin
def c():
    tim.penup()
    tim.clear()
    tim.home()


screen.onkeypress(fun=w(), key="w")
screen.onkeypress(fun=s(), key="s")
screen.onkeypress(fun=a(), key="a")
screen.onkeypress(fun=d(), key="d")
screen.onkeypress(fun=c(), key="c")
screen.listen()

screen.exitonclick()


