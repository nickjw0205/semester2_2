import random

random_num = random.randint(1,100)

print("자! 숫자를 입력해주세요!")
guess = int(input("숫자를 입력해주세여: "))
while(guess != random_num):
	if(guess > random_num):
		print("너무 커영")
	elif(guess < random_num):
		print("너무 작아영")
	guess = int(input("숫자를 입력해주세여: "))

print("정답입니다!")
