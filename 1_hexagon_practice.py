import turtle
tt=turtle.Turtle()

def print_goto(p_x,p_y):
    tt.penup()
    tt.goto(p_x,p_y)
    tt.pendown()

def draw_hexagon(p_length):
    for i in range(6):
        tt.forward(p_length)
        tt.right(60)

for i in range(3):
    print_goto(i * 200 - 300,300)
    draw_hexagon(i * 20 + 40)

