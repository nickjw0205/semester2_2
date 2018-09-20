weight = int(input("몸무게를 입력해주세요: "))
height = float(input("키를 입력해주세요: "))

BMI = weight / (height/100)*(height/100)

# print("당신의 BMI 수치는 ", BMI, "입니다.")
print("당신의 BMI 수치는 %.2f 입니다." %BMI)