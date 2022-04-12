import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    john = turtle.Turtle()
    john.shape("turtle")
    john.color("green")
    john.speed(5)
    john.forward(150)
    john.right(55)
    john.left(65)
    window.exitonclick()

draw_square()
