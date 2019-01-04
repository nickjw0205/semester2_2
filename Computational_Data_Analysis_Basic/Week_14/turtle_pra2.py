import turtle as t

def turn_right():
	t.setheading(0)
	t.forward(10)

def turn_up():
	t.setheading(90)
	t.forward(10)

def turn_left():
	t.setheading(180)
	t.forward(10)

def turn_down():
	t.setheading(270)
	t.forward(10)

def black():
	t.clear()


t.shape("turtle")

#키보드 입력
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_up, "Up")
t.onkeypress(black, "Escape")
t.listen()

t.exitonclick()
# time.sleep(5)