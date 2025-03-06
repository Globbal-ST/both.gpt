from turtle import *
from time import sleep
import random

colors = ['red', 'orange','yellow','green','blue','violet']
random_color = random.choice(colors)
shape("turtle")
pensize(5)
print("Загрузка данных...")
sleep(5)
print("Версия BothGPT: 2.0")
sleep(2)
print("Привет! Это чат-бот который рисует фигуры, и выполняет комманды 🦄. Начнём?")
print("Смотри ниже :wink:, где окно рисования!")
while True:
    zapros_paint = input('Введи желаемую фигуру (или "хватит" для завершения): ').strip().lower()
    break
pencolor(random.choice(colors))

if zapros_paint == "хватит":
    print("Выход из программы. Возращяйся!")
    for i in range(1):
        break
elif zapros_paint == '?' and zapros_paint == 'help' and zapros_paint == 'помощь':
    print("Список доступных фигур:")
    print("Дыры")
    print("Дыра -  нарисует чёрную дыру.")
    print("Полноэкранная дыра - нарисует дыру только на весь экран")
    print("Ромбовая дыра - нарисует дыру только чуть чуть другую с углом поворота 70")
    print("Ромбовая полноэкранная дыра - ромбовая дыра, только на полный экран")
elif zapros_paint == 'нарисуй круг':
    circle(70)
elif zapros_paint == 'нарисуй квадрат':
    for i in range(4):
        forward(70)
        left(90)
elif zapros_paint == 'нарисуй треугольник':
    for i in range(3):
        forward(70)
        left(120)
elif zapros_paint == 'нарисуй звезду':
    for i in range(5):
            forward(100)
            left(144)
elif zapros_paint == 'нарисуй дыру':
    pensize(2)
    speed('fastest')
    for i in range(300):
        forward(i)  # Use the i variable for the function argument.
        left(91)
elif zapros_paint == 'нарисуй красный ремешок':
    pensize(2)
    fillcolor('red')
    pensize(10)
    pencolor('black')
    forward(100)
    begin_fill()
    forward(100)    
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    end_fill()
elif zapros_paint == 'нарисуй фиолетовый ремешок':
    pensize(2)
    fillcolor('purple')
    pensize(10)
    pencolor('black')
    forward(100)
    begin_fill()
    forward(100)    
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    end_fill()
elif zapros_paint == 'нарисуй ремешочек зелёный':
    pensize(2)
    fillcolor('green')
    pensize(10)
    pencolor('black')
    forward(100)
    begin_fill()
    forward(100)    
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    end_fill()
elif zapros_paint == 'нарисуй прямоугольник':
    for i in range(2):
        forward(70)
        left(90)
        forward(30)
        left(90)
elif zapros_paint == 'нарисуй перевёрнутую шесть':
    penup()
    for i in range(30, -1, -1):
        stamp()
        left(i)
        forward(20)
elif zapros_paint == 'нарисуй полноэкранную дыру':
    pensize(2)
    speed('fastest')
    for i in range(500):
        forward(i)  # Use the i variable for the function argument.
        left(91)
elif zapros_paint == 'нарисуй ромбовую дыру':
    pensize(2)
    speed('fastest')
    for i in range(300):
        forward(i)  # Use the i variable for the function argument.
        left(70)
elif zapros_paint == 'нарисуй ромбовую полноэкранную дыру':
    pensize(2)
    speed('fastest')
    for i in range(500):
        forward(i)  # Use the i variable for the function argument.
        left(70)
elif zapros_paint == 'нарисуй тупой угол':
    forward(70)
    left(45)
    forward(70)
elif zapros_paint == 'нарисуй прямой угол':
    forward(70)    
    left(90)
elif zapros_paint == 'нарисуй лианы':
    pensize(2)
    speed('fastest')
    for i in range(5000):
        circle(300)
elif zapros_paint == 'нарисуй верёвку':
    pensize(2)
    speed('fastest')
    for i in range(5000):
        circle(3000)
elif zapros_paint == 'нарисуй майнкрафт':
    print("Сам нарисуй!")
elif zapros_paint == 'нарисуй бамбук':
    color("green")
    left(90)
    forward(999)

hideturtle()
exitonclick()
