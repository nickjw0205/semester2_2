import math
# x = int(input("숫자를 입력해 주세요: "))

# d = 2

# while(x >= d):
# 	if(x % d == 0):
# 		print(d)
# 		x = x/d
# 	else:
# 		d += 1

print("ax^2 + bx + c = 0")
a = int(input("a를 입력해주세요: "))
b = int(input("b를 입력해주세요: "))
c = int(input("c를 입력해주세요: "))

if(a == 0):
	print("이차방정식이 아님.")
	sys.exit()

D = b*b - 4*a*c

if(D > 0):
	print("근은 2개 입니다.")
	sol1 = (-b + math.sqrt(D))/(2*a)
	sol2 = (-b - math.sqrt(D))/(2*a)
	print(sol1)
	print(sol2)

elif(D == 0):
	print("근은 한개입니다.")
	sol1 = (-b + math.sqrt(D))/(2*a)
	print(sol1)

else:
	print("해가없습니다.")

