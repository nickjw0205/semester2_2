#SuperClass
class Car:
	speed = 0

	def upSpeed(self, speed):
		self.speed = speed

#SubClass
class Sedan(Car):
	seatNum = 0

	def getSeatNum(self):
		return self.seatNum

#SubClass
class Truck(Car):
	capacity = 0

	#오버라이딩
	def upSpeed(self, speed):
		self.speed = speed

		if self.speed > 110:
			self.speed = 110

	def getCapacity(self):
		return self.capacity





sedan1 = Sedan()
sedan1.upSpeed(100)
sedan1.seatNum = 5

print("세단의 속도는 %d이고, 좌석수는 %d입니다." %(sedan1.speed, sedan1.seatNum))

truck1 = Truck()
truck1.upSpeed(200)
truck1.capacity = 1000

print("트럭의 속도는 %d이고, 중량은 %d입니다." %(truck1.speed, truck1.getCapacity()))