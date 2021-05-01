from turtle import*

speed(10)

penup()
goto(-200,0)
pendown()


def draw_square(sidelength = 30):
    for i in range(4):
        forward(sidelength)
        left(90)

def compute_turn_angle(n = 90):
    return 180 - 180*(n-2)/n

def draw_ngon(n,sidelength = 100):
    for i in range(n):
        forward(sidelength)
        left(compute_turn_angle(n))

draw_ngon(6,100)
done()
