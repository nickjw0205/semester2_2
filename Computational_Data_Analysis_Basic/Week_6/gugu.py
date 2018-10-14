# # for i in range(2,10):
# # 	for j in range(1, 10):
# # 		print("%d x %d = %d" %(i) %(j) %(i*j), end = "")

# guguline = ""

# for i in range(2, 10):
# 	guguline += 	("   #%d단# |" %i)

# print(guguline)

# guguline = ""

# for i in range(1, 10):
# 	for j in range(2, 10):
# 		guguline += ("%2d*%2d=%2d | " %(j, i, j*i))
# 	print(guguline)
# 	guguline = ""

i = 1

while(i != 10):
	j = 2
	while(j != 10):
		print("%2d *%2d = %2d |" %(j, i, i*j), end = " ")
		j += 1
	i += 1
	print()