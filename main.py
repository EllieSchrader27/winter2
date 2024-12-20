import turtle
import random

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("dark red")


t = turtle.Turtle()
t.speed(0)

t_ground = turtle.Turtle()
t_ground.fillcolor("dark khaki")
t_ground.pencolor("dark khaki")
t_ground.speed(0)
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()


move_up_down = -100
move_mantle = move_up_down + 35
move_left_right = -150

t = turtle.Turtle()
colors = ['firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', ]
t.speed(0)
bump = 0
adjust_x = -100
adjust_y = 100
x = -100
y = move_up_down
size_x = 40
brick_x = 8
brick_y = 2.25
scale = size_x / brick_x
size_y = scale * brick_y
t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.end_fill()
x_beg = -20
y_beg = 0
for x in range(15):
    x_beg = x * 20 - 8
    t.penup()
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.pendown()
    col = random.choice(colors)
    t.fillcolor(col)
    t.begin_fill()
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.end_fill()

for j in range(12):
    move_y = j * size_y
    if j % 2 == 0:
        bump = 0
    else:
        x = 0
        bump = size_x / 2
        t.penup()
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.pendown()
        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        t.goto(move_left_right + x + bump + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + x + bump + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()
    for i in range(7):
        x = i * size_x
        if x + bump + size_x > 280:
            size_x = size_x / 2
        else:
            size_x = 40

        start_x = x + bump
        end_x = x + bump + size_x

        t.penup()
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.pendown()

        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        if j >= 3 and j <= 9:
            if end_x > 100 and start_x < 180:
                end_x = 80

                start_x = 200
                t.penup()
                size_x = 40

        t.goto(move_left_right + end_x + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + end_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()

t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.fillcolor('black')
t.begin_fill()
t.goto(move_left_right + 205 + adjust_x, move_up_down - 35 + adjust_y)
t.goto(move_left_right + 205 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.end_fill()

t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.end_fill()



t.penup()
t.goto(90, -150)
t.fillcolor('saddle brown')
t.pendown()
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.end_fill()


t.fillcolor('dark green')
t.pencolor('dark green')

t.penup()
t.goto(0,-115)#1/4
t.pendown()
t.begin_fill()
t.goto(200,-115)
t.goto(100,-15)
t.goto(0,-115)
t.end_fill()

t.penup()
t.goto(25,-45)#1/4
t.pendown()
t.begin_fill()
t.goto(175,-45)
t.goto(100,55)
t.goto(25,-45)
t.end_fill()



t.penup()
t.goto(50,15)#1/4
t.pendown()
t.begin_fill()
t.goto(150,15)
t.goto(100,115)
t.goto(50,15)
t.end_fill()

t.setheading(180)
t.penup()
t.goto(-10,20)
t.pendown()
t.penup()
t.pencolor('purple')
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.end_fill()

t.setheading(180)
t.penup()
t.goto(-30,-10)
t.pencolor('purple')
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.circle(10,180)
t.end_fill()


t.penup()
t.goto(-90,-30)
t.pendown()
t.penup()
t.pencolor('turquoise4')
t.fillcolor('turquoise4')
t.pendown()
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.end_fill()

t.setheading(180)
t.penup()
t.goto(-90,-10)
t.pencolor('turquoise4')
t.fillcolor('turquoise4')
t.pendown()
t.begin_fill()
t.circle(10,180)
t.end_fill()


t.penup()
t.goto(-150,-30)
t.pendown()
t.penup()
t.pencolor('light coral')
t.fillcolor('light coral')
t.pendown()
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.end_fill()

t.setheading(180)
t.penup()
t.goto(-150,-10)
t.pencolor('light coral')
t.fillcolor('light coral')
t.pendown()
t.begin_fill()
t.circle(10,180)
t.end_fill()

t.penup()
t.goto(-210,-30)
t.pendown()
t.penup()
t.pencolor('gold1')
t.fillcolor('gold1')
t.pendown()
t.begin_fill()
t.forward(20)
t.left(90)
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.end_fill()

t.setheading(180)
t.penup()
t.goto(-210,-10)
t.pencolor('gold1')
t.fillcolor('gold1')
t.pendown()
t.begin_fill()
t.circle(10,180)
t.end_fill()

t.penup()
t.goto(150, -150)
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()


t.penup()
t.goto(165, -100)
t.fillcolor('yellow')
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(15)
t.end_fill()


t.pencolor('yellow')
t.pensize(2)
t.penup()
t.goto(165,-80)
t.pendown()
t.circle(10)
t.penup()
t.goto(175,-80)
t.pendown()
t.circle(10)


t.penup()
t.goto(-150,200)
t.pencolor("black")
t.fillcolor('green')
t.pendown()
t.begin_fill()
t.circle(50)
t.penup()
t.end_fill()

t.goto(-150,175)
t.fillcolor('dark red')
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(295,275)
t.pencolor('black')
t.fillcolor('CornflowerBlue')
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(140)
t.left(90)
t.forward(150)
t.left(90)
t.forward(140)
t.end_fill()


for i in range(50):
   t.pencolor('white')
   t.penup()
   x = random.randint(155,285)
   y = random.randint(135,275)
   t.goto(x,y)
   z = random.randint(0,3)
   t.pendown()
   t.pensize(z)
   t.dot()




t.pencolor('black')
t.pensize(3)
t.penup()
t.goto(220,280)
t.setheading(270)
t.pendown()
t.forward(150)


t.penup()
t.goto(150,205)
t.setheading(0)
t.pendown()
t.forward(140)

t.penup()
t.goto(-10,250)
t.write("Merry Christmas",font=("Calibri",50," italic"), align ="center")

t.penup()
t.goto(100,-100)
t.pencolor('MidnightBlue')
t.fillcolor('MidnightBlue')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.goto(80,20)
t.pencolor('red')
t.fillcolor('red')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.goto(100,-20)
t.pencolor('yellow')
t.fillcolor('yellow')
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()


t.penup()
t.goto(-160,200)
t.pencolor('red')
t.pendown()
t.circle(10)




t.penup()
t.goto(-140,200)
t.pencolor('red')
t.pendown()
t.circle(10)



turtle.done()