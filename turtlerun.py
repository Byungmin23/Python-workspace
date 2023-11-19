#te = 악당 거북이
#point = 

import turtle as t
import random

te = t.Turtle() # 악당 거북이(빨간색))
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

point = t.Turtle() # 먹이(초록색 동그라미)
point.shape("circle")
point.color("#FFFF96")
point.speed(0)
point.up()
point.goto(0, -200)

game_over = t.Turtle()
game_over.hideturtle()
game_over.speed(0)
game_over.up()

def game_over_message(m1, m2): 
    score_point.clear()
    game_over.clear()
    game_over.color("white")
    game_over.goto(0, 100)
    game_over.write(m1, False, "center", ("", 20))
    game_over.goto(0, -100)
    game_over.write(m2, False, "center", ("", 20))
    t.home()

score_point = t.Turtle()
score_point.hideturtle()
score_point.speed(0)
score_point.up()

def score_message(m1):
    game_over.clear()
    score_point.clear()
    score_point.write(m1, False, "center", ("", 20, "bold"))
    score_point.goto(0, 0)

def turn_right(): # 오른쪽으로 방향 전환
    t.setheading(0)
def turn_up(): # 위쪽으로 방향 전환
    t.setheading(90)
def turn_left(): # 왼쪽으로 방향 전환
    t.setheading(180)
def turn_down(): # 아래쪽으로 방향 전환
    t.setheading(270)

playing = False # 현재 게임이 플레이 중인지 확인하는 변수

def start(): # 게임을 시작하는 함수
    global playing

    if playing == False:
        playing = True
        t.clear() # 화면에 메시지를 지운다
        score_point.clear()
        score_point.goto(0, 0)
        score_message(f"Score : {score}")
        play()

score = 0 # 점수를 저장하는 변수

def play():
    global score
    global playing

    t.forward(10)

    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5

    if speed > 15:
        speed = 15

    te.forward(speed)
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        te.goto(0, 200)
        te.setheading(-90)
        point.goto(0, -200)
        game_over_message("Game Over", text)
        t.home()
        t.color("#429F6B")
        playing = False
        score = 0

    if t.distance(point) < 12: # 먹이의 거리가 12보다 작으면
        score = score + 1 # 점수를 올리고
        score_message(f"Score : {score}") # 화면에 점수를 출력 합니다.
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        point.goto(start_x, start_y)
    
    if playing: # 게임 플레이 중이면
        t.ontimer(play, 100) # 0.1초 후 play 함수 실행
    
t.setup(500, 500)
t.bgcolor("#A0A0FF")

t.shape("turtle")
t.speed(0)
t.setheading(270)
t.up()
t.color("#429F6B")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, 'space')

t.listen()
play() # play 함수를 호출해서 게임을 시작

t.mainloop()
