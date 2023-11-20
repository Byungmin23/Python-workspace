import turtle as t
import random
from threading import Timer

# 악당 거북이(빨간색) 설정
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)
te.setheading(-90)

# 점수 획득을 위한 포인트(노랑) 설정
point = t.Turtle()
point.shape("circle")
point.color("#FFFF96")
point.speed(0)
point.up()
point.goto(0, -200)

# 게임 오버를 표시할 거북이 설정
game_over = t.Turtle()
game_over.hideturtle()
game_over.speed(0)
game_over.up()

# 점수를 화면에 표시할 거북이 설정
score_point = t.Turtle()
score_point.hideturtle()
score_point.speed(0)
score_point.up()

# 초기 화면에 메시지를 보여줄 거북이 설정
popup = t.Turtle()
popup.hideturtle()
popup.speed(0)
popup.up()

# 초기 메시지 표시 함수
def first_message():
    popup.color("white")
    popup.goto(0, 100)
    popup.write("Turtle Run Game", False, "center", ("", 20, "bold"))
    popup.goto(0, 70)
    popup.write("if you play turtle run game, pass spacr bar", False, "center", ("", 10, "bold"))

# 빠른 악당 거북이(주황색) 추가 함수
def add_bed_te():
    global eadd_te_list  # 악당 거북이(주황색) 리스트를 전역 변수로 사용
    global add_te

    add_te = t.Turtle()  # 새로운 악당 거북이(주황색) 생성
    add_te.shape("turtle")
    add_te.color("orange")
    add_te.speed(0)  # 기존 악당 거북이와 속도 동일하게 설정
    add_te.up()
    start_x = random.randint(-230, 230)
    start_y = random.randint(-230, 230)
    add_te.goto(0, 0)
    add_te_list.append(add_te)  # 새로운 악당 거북이(주황색)를 리스트에 추가
    
    Timer(10, remove_add_te, args=(add_te,)).start()  # 새로운 악당 거북이(주황색) 삭제 타이머 설정

# 새로운 악당 거북이(주황색) 삭제 함수
def remove_add_te(add_te):
    add_te.hideturtle()  # 악당 거북이 숨기기
    add_te.goto(1000, 1000)  # 화면 밖으로 이동(제거되지 않은 거북이를 위한 안전장치)
    add_te.remove(add_te)  # 리스트에서 제거

# 악당 거북이들을 담을 리스트
add_te_list = []
add_tetimers = []  # 악당 거북이 타이머를 담을 리스트

# 새로운 악당 거북이(주황색) 이동 함수
def move_add_te():
    global score  # 전역 변수 설정
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

# 게임 오버 메시지와 거북이 초기 설정 함수
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

# 점수 표시 함수
def score_message(m1):
    game_over.clear()
    score_point.clear()
    score_point.color("white")
    score_point.write(m1, False, "center", ("", 20, "bold"))
    score_point.goto(0, 210)

# 방향 전환 함수들
def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

playing = False  # 게임 실행 중인지 확인하는 변수
score = 0  # 점수를 저장하는 변수

# 게임 시작 함수
def start():
    global playing

    if not playing:
        playing = True
        t.clear()  # 화면 초기화
        score_point.clear()
        score_point.goto(0, 210)
        score_message(f"Score : {score}")
        popup.clear()
        play()

# 메인 게임 루프
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

        if score % 3 == 0 and score != 0:
            add_bed_te()

    if playing:
        move_add_te()
        t.ontimer(play, 100)

# 터틀 화면 및 키 설정
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
play()  # 게임 시작

t.mainloop()
