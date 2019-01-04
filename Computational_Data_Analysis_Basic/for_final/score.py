import random

def average(a):
	avg = 0
	for i in a:
		avg += i
	return avg/len(a)


def hl(a, answer):
	if a == answer:
		return 1
	elif a > answer:
		return 2
	else:
		return 3

answer = random.randint(1,100)
user = int(input("입력: "))
hol = hl(user, answer)
while(hol != 1):
	if(hol == 2):
		print("너무 큼!")
	else:
		print("작음!")
	user = int(input("입력: "))
	hol = hl(user, answer)
print("Good job!")