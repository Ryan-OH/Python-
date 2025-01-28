import turtle
import random

class ChristmasMessage:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Merry Christmas!")
        self.screen.bgcolor("lightblue")  # 배경색을 크리스마스 분위기로 설정
        self.t = turtle.Turtle()
        self.screen.onclick(self.display_message)
        self.messages = []  # 이미 그린 글씨의 위치를 저장할 리스트
        
    def is_position_valid(self, x, y, width, height):
        for msg_x, msg_y, msg_width, msg_height in self.messages:
            if (x < msg_x + msg_width and x + width > msg_x and
                y < msg_y + msg_height and y + height > msg_y):
                return False
        return True
    
    def display_message(self, x, y):
        colors = ['red', 'green', 'gold', 'white']
        font_styles = ['Arial', 'Comic Sans MS', 'Courier New']
        
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        self.t.hideturtle()
        self.t.clear()
        
        attempts = 0
        max_attempts = 100  # 무한 루프를 방지하기 위해 최대 시도 횟수 설정
        
        for _ in range(10):  # 여러 개의 메시지를 랜덤 위치에 표시
            while attempts < max_attempts:
                attempts += 1
                rand_color = random.choice(colors)
                rand_font = random.choice(font_styles)
                rand_size = random.randint(24, 72)
                rand_x = random.randint(-self.screen.window_width() // 2 + rand_size * 5, 
                                        self.screen.window_width() // 2 - rand_size * 5)
                rand_y = random.randint(-self.screen.window_height() // 2 + rand_size, 
                                        self.screen.window_height() // 2 - rand_size)
                
                width = len("MERRY CHRISTMAS! 🎄✨") * rand_size // 2
                height = rand_size
                
                if self.is_position_valid(rand_x, rand_y, width, height):
                    self.messages.append((rand_x, rand_y, width, height))
                    break
            
            self.t.penup()
            self.t.goto(rand_x, rand_y)
            self.t.pendown()
            self.t.color(rand_color)
            
            style = (rand_font, rand_size, 'bold')
            self.t.write("MERRY CHRISTMAS! 🎄✨", align='center', font=style)

# ChristmasMessage 객체 생성
message = ChristmasMessage()

# 터틀 그래픽 창 유지하기
turtle.done()
