import turtle as t
import random
from threading import Timer


te = t.Turtle()  # 악당 거북이(빨간색))
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)
te.setheading(-90)

point = t.Turtle()  # 먹이(초록색 동그라미)
point.shape("circle")
point.color("#FFFF96")
point.speed(0)
point.up()
point.goto(0, -200)

game_over = t.Turtle()
game_over.hideturtle()
game_over.speed(0)
game_over.up()

score_point = t.Turtle()
score_point.hideturtle()
score_point.speed(0)
score_point.up()

popup = t.Turtle()
popup.hideturtle()
popup.speed(0)
popup.up()

def first_message():
    popup.color("white")
    popup.goto(0, 100)
    popup.write("Turtle Run Game", False, "center", ("", 20, "bold"))
    popup.goto(0, 70)
    popup.write("if you play turtle run game, pass spacr bar", False, "center", ("", 10, "bold"))
    

def add_bed_te():
    global eadd_te_list  # 전역 변수로 악당 거북이 리스트 사용
    global add_te

    add_te = t.Turtle()  # 새로운 악당 거북이 생성
    add_te.shape("turtle")
    add_te.color("orange")
    add_te.speed(0) # 기존 거북이의 속도 설정
    add_te.up()
    start_x = random.randint(-230, 230)
    start_y = random.randint(-230, 230)
    add_te.goto(0, 0)
    add_te_list.append(add_te)  # 새로운 악당 거북이 리스트에 추가
    
    Timer(10, remove_add_te, args=(add_te,)).start()  # 악당 거북이 삭제 타이머
    #display_time()

def remove_add_te(add_te):
    add_te.hideturtle()  # 악당 거북이 숨기기
    add_te.remove(add_te)  # 리스트에서 제거

add_te_list = []  # 악당 거북이들을 담을 리스트 생성
add_tetimers = []  # 악당 거북이 타이머를 담을 리스트 생성

def move_enemies():
    global score
    global playing

    for add_te in add_te_list:
        add_te.setheading(add_te.towards(t.pos()))  # 플레이어를 향해 이동
        add_te.forward(speed)  # 악당 거북이 움직임

        # 플레이어와 악당 거북이의 거리 확인
        if t.distance(add_te) < 12:
            text = "Score : " + str(score)
            te.goto(0, 200)
            te.setheading(-90)
            point.goto(0, -200)
            game_over_message("Game Over", text)
            t.goto(0, 0)
            t.color("#429F6B")
            playing = False
            score = 0

def game_over_message(m1, m2):
    global add_te_list
    global add_te

    score_point.clear()
    game_over.clear()
    game_over.color("white")
    game_over.goto(0, 100)
    game_over.write(m1, False, "center", ("", 20, "bold"))
    game_over.goto(0, 70)
    game_over.write(m2, False, "center", ("", 20, "bold"))
    t.goto(0, 0)
    t.setheading(-90)
    te.goto(0, 200)

    for add_te in add_te_list:
        add_te.hideturtle()
    add_te_list = []
    

def score_message(m1):
    game_over.clear()
    score_point.clear()
    score_point.color("white")
    score_point.write(m1, False, "center", ("", 20, "bold"))
    score_point.goto(0, 210)

def turn_right():  # 오른쪽으로 방향 전환
    t.setheading(0)

def turn_up():  # 위쪽으로 방향 전환
    t.setheading(90)

def turn_left():  # 왼쪽으로 방향 전환
    t.setheading(180)

def turn_down():  # 아래쪽으로 방향 전환
    t.setheading(270)

playing = False  # 현재 게임이 플레이 중인지 확인하는 변수
score = 0  # 점수를 저장하는 변수

def start():  # 게임을 시작하는 함수
    global playing

    if not playing:
        playing = True
        t.clear()  # 화면에 메시지를 지운다
        score_point.clear()
        score_point.goto(0, 210)
        score_message(f"Score : {score}")
        popup.clear()
        play()


def play():
    global score
    global playing
    global speed

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
        t.goto(0, 0)
        t.color("#429F6B")
        playing = False
        score = 0


    if t.distance(point) < 12:  # 먹이의 거리가 12보다 작으면
        score += 1  # 점수를 올리고
        score_message(f"Score : {score}")  # 화면에 점수를 출력합니다.
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        point.goto(start_x, start_y)

        if score % 1 == 0 and score != 0:  # score가 5의 배수이고 0이 아닐 때
            add_bed_te()  # 악당 거북이 추가

    if playing:  # 게임 플레이 중이면
        move_enemies()  # 악당 거북이 이동
        t.ontimer(play, 100)  # 0.1초 후 play 함수 실행

t.setup(500, 500)
t.bgcolor("#A0A0FF")
first_message()
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
