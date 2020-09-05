import turtle
tt=turtle.Turtle()

def print_goto(p_x,p_y):
    tt.penup()
    tt.goto(p_x,p_y)
    tt.pendown()



def draw_hexagon(p_length):
    print(50)
    for i in range(6):
        tt.forward(p_length)
        tt.right(60)
print_goto(-600,300)
draw_hexagon(50)

print_goto(-400,300)
draw_hexagon(70)
print_goto(-200,300)
draw_hexagon(90)
