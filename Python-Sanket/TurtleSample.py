import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(29999999)

    i = 0
    while i < 4:
        brad.forward(100)
        brad.right(90)
        i += 1


    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("cyan")
    angie.circle(20)

    garry = turtle.Turtle()
    garry.shape("triangle")
    garry.color("green")

    j = 0

    while j < 3:
       garry.forward(50)
       garry.left(120)
       j += 1

    window.exitonclick()

draw_square()
