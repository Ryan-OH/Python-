import turtle
import random

class RectangleDrawer:
    def __init__(self):
        self.t = turtle.Turtle()
        turtle.onscreenclick(self.draw_random_rectangle)

    def draw_random_rectangle(self, x, y):
        width = random.randint(50, 200)
        height = random.randint(50, 200)
        pen_size = random.randint(1, 10)
        fill_color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
        
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.pensize(pen_size)
        self.t.color(fill_color, fill_color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.right(90)
            self.t.forward(height)
            self.t.right(90)
        self.t.end_fill()

drawer = RectangleDrawer()

turtle.done()
