import random
import time
# def car1(color, speed):
# 	print("자동차1의 색상은 %s이고, 속도는 %d입니다." %(color, speed))

# car1("삘강", 30)
# car1("파랑", 60)

class Car:
	color = ""
	speed = 0
	count = 0
	def __init__(self, color, speed):
		self.color = "빨강"
		self.color = color
		self.speed = speed
		Car.count += 1

myCar1 = Car("빨강", 30)
print("자동차1의 색상은 %s이고, 속도는 %d입니다." %(myCar1.color, myCar1.speed))


myCar2 = Car("파랑", 20)
print("자동차2의 색상은 %s이고, 속도는 %d입니다." %(myCar2.color, myCar2.speed))

print("자동차가 %d대 있습니다." %(Car.count))

Color_list = ["빨강", "파랑", "노랑", "주황", "초록", "보라"]
while(True):
	num = random.randint(0,5)
	myCar = Car(Color_list[num], random.randint(1,100))
	print("자동차의 색상은 %s이고, 속도는 %d입니다." %(myCar.color, myCar.speed))
	print("자동차가 %d대 있습니다." %(Car.count))
	time.sleep(1)
