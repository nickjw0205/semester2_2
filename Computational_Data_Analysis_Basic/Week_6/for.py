names = ['kim','Kee','kie']

# index = 0

# for i in names:
# 	names[index] = "Mr." + i
# 	index += 1

#for i in range(0, 10, 2):		# ->0 2 4 6 8
#	print(i)

# for i in range(0,3):
# 	for j in names[i]:
# 		for z in j:
# 			print(z, end = "")
# 	print()

input = int(input("몇 !을 계산 하시겠습니까??: "))

result = 1

for i in range(1,input+1):
	result *= i

print(input, "! = ", result)

