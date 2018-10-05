num1 = int(input("당신의 점수를 입력해주세요: "))

if num1 > 100:
	print("거짓말 하지마")
elif num1 >= 90:
	print("A")
elif num1 >= 80:
	print("B")
elif num1 >= 70:
	print("C")
elif num1 >= 60:
	print("D")
elif num1 >= 50:
	print("E")
else:
	print("넌 F란다. 사람이니??")