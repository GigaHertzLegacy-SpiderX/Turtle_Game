# Coded by SpiderX360

# modules
import turtle as tt
import random

# Screen
tt.Screen()
tt.title("Turtle Game !")
tt.speed(0)

# Moving Part

walk = int(tt.textinput(title="Walk input", prompt="Define Turtle Walk Space !")).__floor__()


def Walk_up():
    tt.forward(walk)


def Walk_down():
    tt.back(walk)


def Walk_right():
    tt.right(90)
    # tt.forward(walk)


def Walk_left():
    tt.left(90)
    # tt.forward(walk)


def Middle():
    tt.penup()
    tt.setx(0)
    tt.sety(0)
    tt.pendown()


def Hide_turtle():
    tt.hideturtle()


def Show_turtle():
    tt.showturtle()


def Change_color():
    color = ['black', 'blue', 'red', 'white', 'green', 'gold', 'maroon', 'violet', 'magenta', 'purple', 'navy',
             'skyblue', 'cyan', 'turquoise', 'lightgreen', 'darkgreen', 'chocolate', 'brown', 'gray']

    tt.bgcolor(f"{color[random.randrange(0, len(color))]}")


def Pen_color():
    color = ['black', 'blue', 'red', 'white']
    tt.pencolor(f"{color[random.randrange(0, len(color))]}")


def Exit():
    tt.bye()
    print("Exited...")


# def Save_image():
# ts = tt.getscreen()
# tt.getcanvas().postscript(file="image.emp")


while True:
    # Listerner
    tt.listen()
    tt.onkeypress(Walk_up, 'w')
    tt.onkeypress(Walk_left, 'a')
    tt.onkeypress(Walk_right, 'd')
    tt.onkeypress(Walk_down, 's')
    tt.onkeypress(Middle, 'm')
    tt.onkeypress(Change_color, 'c')
    tt.onkeypress(Pen_color, 'p')
    tt.onkeypress(Hide_turtle, 'h')
    tt.onkeypress(Show_turtle, 'H')
    tt.onkeypress(Exit, 'q')
    # tt.onkeypress(Save_image, 'k')
    tt.update()
    tt.done()


# Need Update
"""

1. Saving Canvas
2. Change Turtle Walk Move in running Program
3. Change Title in Running Program
4. Fill Color Live
5. Auto Round Shape 

"""
