import turtle as t
import random

# 악당 거북이
te = t.Turtle()
te.shape("turtle")
te.color("red")

# 0이 가장 빠름, 선이 그어지면 안되므로 up()을 사용함
te.speed(0)
te.up()
te.goto(0,200)

# 전역변수 설정
score = 0 
speed = 1 
playing = False 

# 원 생성 -> 먹이 색성
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    # 그쪽의 각을 바라 보는 것 // 오른쪽이 0도 이다
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def black():
    t.clear()

def play():
    global speed 
    t.forward(10)
    
    # t의 위치를 구함 t.pos()
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(speed)

    # 아이템을 먹는 것
    if t.distance(ts) < 12 :
        # 왼쪽은 지역변수, 오른쪽은 전역변수로 되기 때문에.. 지렸다
        global score
        score = score +1
        speed = speed + 1
        t.write(score)
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,230)
        ts.goto(star_x,star_y)

    # 적 거북이랑 만나지 않는 것 -> 만나면 종료가 됨
    if t.distance(te) >=  12 :
        # 단위가 ms 임 / 0.1 초 후에 play를 다시 실행시킴
        t.ontimer(play,100)
    else :
        # False : 글자를 입력하고 거북이를 옮기지 않겠다는 것이다
        t.write("Game Over",False,"center",("",20))

def start():
    global playing
    if playing == False :
        playing = True 
        t.clear()
        play()


# 창 크기 설정
t.setup(500,500)
t.bgcolor("orange")

# 사용자 거북이 만들기
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

# 키보드 입력 받기
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

# 스페이스는 소문자로 이용해야한다
t.write("Space 클릭 후 게임 시작",False,"center",("",20))
t.onkeypress(start,"space")
t.listen()

# 창이 바로 종료 되지 않기 위해서 넣어놓음 -> 창을 클릭하면 종료되는 함수
t.exitonclick()