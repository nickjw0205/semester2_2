while(True):
	num1 = int(input("첫번째 숫자를 입력해 주세요: "))
	operator = input("연산자를 입력해 주세요: ")
	num2 = int(input("두번째 숫자를 입력해 주세요: "))
	
	if(operator == '%'):
		print("%d %s %d = %d" %(num1, operator, num2, num1 % num2))
	elif(operator == "*"):
		print("%d %s %d = %d" %(num1, operator, num2, num1 * num2))
	elif(operator == "+"):
		print("%d %s %d = %d" %(num1, operator, num2, num1 + num2))
	elif(operator == "-"):
		print("%d %s %d = %d" %(num1, operator, num2, num1 - num2))
	elif(operator == "/"):
		print("%d %s %d = %f" %(num1, operator, num2, num1 / num2))
	elif(operator == "//"):
		print("%d %s %d = %d" %(num1, operator, num2, num1 // num2))
	elif(operator == "**"):
		print("%d %s %d = %f" %(num1, operator, num2, num1 ** num2))