import turtle as t
import random

te = t.Turtle() #악당 거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle() #먹이
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right(): #오른쪽으로 전환
    t.setheading(0)

def turn_up(): #위쪽으로 전환
    t.setheading(90)

def turn_left(): #왼쪽으로 전환
    t.setheading(180)

def turn_down(): #아래쪽으로 전환
    t.setheading(270)

def play(): #게임 진행 함수
    t.forward(10) #주인공 거북이가 10만큼 앞으로 이동

    ang = te.towards(t.pos()) #악당 거북이가 주인공 거북이를 향해 전환
    te.setheading(ang)

    te.forward(9) #악당 거북이가 9만큼 이동

    if t.distance(ts) < 12: #주인공과 먹이의 거리가 12보다 작으면
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        ts.goto(start_x, start_y) #먹이를 다른 곳으로 이동

    if t.distance(te) >= 12: #주인공과 악당의 거리가 12이상이면
        t.ontimer(play, 100) #0.1초 후 play 함수 실행(게임 계속)

t.setup(500, 500)
t.bgcolor("orange")

t.shape("turtle")
t.speed(0)
t.up
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

t.listen()
play()

t.mainloop()