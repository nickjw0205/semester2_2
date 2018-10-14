a = [0,0,0,0]
total = 0

for i in range(0,4):
	a[i] = int(input(str(i+1) + "번째 숫자: "))
	total += a[i]

print(total)