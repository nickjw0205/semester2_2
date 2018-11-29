def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def mul(n1, n2):
	return n1*n2

def div(n1, n2):
	return n1 / n2

while(True):
	a = int(input("무슨 연산을 하시겠습니까??(1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 종료)"))
	if(a == 5):
		break;

	else:
		num1 = int(input("정수 1: "))
		num2 = int(input("정수 2: "))
		if(a == 1):
			print("%d + %d = %d\n"%(num1, num2, add(num1,num2)))
		elif(a == 2):
			print("%d - %d = %d\n"%(num1, num2, sub(num1,num2)))
		elif(a == 3):
			print("%d * %d = %d\n"%(num1, num2, mul(num1,num2)))
		else:
			print("%d / %d = %d\n"%(num1, num2, div(num1,num2)))
