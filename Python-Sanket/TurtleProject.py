import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(29)

    i = 0
    while True:
        brad.forward(30)
        brad.right(200)
        brad.forward(10)
        brad.right(250)
        brad.forward(30)

    window.exitonclick()

draw_art()