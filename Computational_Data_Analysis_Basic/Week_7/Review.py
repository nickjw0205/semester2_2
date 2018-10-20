#-----review 1----------
# while(True):
# 	a = int(input("숫자 입력"))

# 	if a == 0:
# 		break
# 	elif a % 2 == 0:
# 		print("짝수 입니다.")
# 	else:
# 		print("홀수 입니다.")

#-----review 2----------
# for i in range(1, 40):
# 	if i % 5 == 0:
# 		print(i, end=" ")
# print()

# names = ['kim', 'Park', 'Seo', 'lee']

# index = 0

# for i in names:
# 	if i == 'kim':
# 		names[index] = "Mr." + i
# 		print(names[index])
# 		index += 1

# 	elif i == 'Park':
# 		names[index] = "Ms." + i
# 		print(names[index])
# 		index += 1

# 	else:
# 		names[index] = "Mr." + i
# 		print(names[index])
# 		index += 1

names = ["kim", "Park", "Seo", "lee", 1, 2]

# for i in names:
# 	if type(i) == str:
# 		print(i, "는 문자입니다")

# 	else:
# 		print(i, "는 숫자입니다")

index = 0
while(index < len(names)):
	if(type(names[index]) == str):
		print(names[index], "는 문자입니다")
	else:
		print(names[index], "는 숫자입니다")
	index += 1



