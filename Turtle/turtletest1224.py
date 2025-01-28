import turtle

class RectangleDrawer:
    def __init__(self):
        self.t = turtle.Turtle()

    def draw_rectangle(self, width, height, x, y, fill_color, pen_size):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.pensize(pen_size)
        self.t.color('black', fill_color) 
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(width)
            self.t.right(90)
            self.t.forward(height)
            self.t.right(90)
        self.t.end_fill()

# RectangleDrawer 객체 생성
drawer = RectangleDrawer()

drawer.draw_rectangle(100, 50, 0, 0, 'red', 2)

drawer.draw_rectangle(150, 80, -200, 100, 'blue', 4)

drawer.draw_rectangle(70, 140, 100, -100, 'green', 6)

drawer.draw_rectangle(120, 120, 200, 200, 'yellow', 8)

drawer.draw_rectangle(180, 150, 300, -200, 'purple', 10)
# 터틀 그래픽 창 닫기
turtle.done()
