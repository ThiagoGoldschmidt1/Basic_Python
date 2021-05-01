from turtle import*

#sets speed
speed(10)

#starting point
penup()
goto(-200,0)
pendown()

# our draw_square function draws a square and takes its lengh as parameter. Uses 30 as default
def draw_square(sidelength = 30):
    #for loop to enumerate the turns
    for i in range(4):
        forward(sidelength)
        left(90)

# Computes the turning angle for an n-gon. Basically which angle does each corner of an n-gon has
def compute_turn_angle(n):
    return 180 - 180*(n-2)/n

# draws an n-gon and takes as parameters number of sides(n) and the length of each side (sidelength)
def draw_ngon(n,sidelength = 100):
    #takes n to determine how often it turns
    for i in range(n):
        forward(sidelength)
        #uses our compute_turn_angle function to calculate the angle
        left(compute_turn_angle(n))

draw_ngon(6,100)
done()
