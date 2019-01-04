import turtle as t

# t.color("purple")
# t.begin_fill()
# # n = 5
# # for i in range(n):
# # 	t.forward(100)
# # 	t.left(360/n)

# # t.end_fill()

# n = 90
# t.bgcolor("black")
# t.color("green")
# t.speed(0)
# for i in range(n):
# 	t.circle(80)
# 	t.left(360/n)

# n = 90
# t.bgcolor("white")
# t.color("green")
# t.speed(0)
# for i in range(200):
# 	t.forward(i)
# 	t.left(n)

t.bgcolor("black")
t.speed(0)
for i in range(200):
	if(i % 3 == 0):
		t.color("blue")
	elif(i % 3 == 1):
		t.color("yellow")
	else:
		t.color("red")

	t.forward(i*2)
	t.left(60)