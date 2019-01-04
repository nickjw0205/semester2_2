import turtle as t
import time
import math

x_min = -5
x_max = 5
y_min = -5
y_max = 5

space = 0.1

func = "y=abs(x)"
func1 = "y = x * x"
func2 = "y = 0.5*x + 1"

func_list = ["y=abs(x)","y = x * x","y = 0.5*x + 1"]

#축의 최대최소좌표 입력
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(5)
t.pensize(2)

#이제부턴 이동시킬때 출력이 안된다.
t.up()

#이제 이동을 하자
t.goto(x_min,0)

t.down()
t.goto(x_max,0)

t.up()
t.goto(0,y_min)

t.down()
t.goto(0,y_max)

t.color("green")

#""안의 결과값을 구함
# a = eval("3+4")
#print(a) => 7
#함수를 구하라
# a = exec("y = 3+4")
#print(a) => 7

for i in func_list:
	x = x_min
	exec(i)
	t.up()
	t.goto(x,y)
	t.down()
	while(x <=x_max):

		x = x + space
		exec(i)
		t.goto(x,y)

# t.color("red")
# x = x_min
# exec(func1)
# t.up()
# t.goto(x,y)
# t.down()

# while(x <= x_max):
# 	x = x + space
# 	exec(func1)
# 	t.goto(x,y)

# t.color("blue")
# x = x_min
# exec(func2)
# t.up()
# t.goto(x,y)
# t.down()

# while(x <= x_max):
# 	x = x + space
# 	exec(func2)
# 	t.goto(x,y)



time.sleep(3)




