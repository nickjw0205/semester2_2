import random

def make_quextion():
	a = random.randint(1,40)
	b = random.randint(1,20)
	c = random.randint(1,3)

	q = str(a)

	if(c == 1):
		q += "+"
	elif(c == 2):
		q += "-"
	else:
		q += "*"

	q += str(b)
	return q

answer = 0
user = 0

for x in range(5):
	q = make_quextion()
	print(q)
	ans = input("=")
	r = int(ans)

	if(eval(q) == r):
		print("correct")
	else:
		print("wrong!")
