eng = int(input("영어점수 입력: "))
mat = int(input("수학점수 입력: "))

total = mat + eng

if total < 110:
	print("총점 미달 불합격")
elif eng >= 40:
	if mat >= 40:
		print("합겨어어어어어억")
	else:
		print("수학 점수 미달 불합겨거엉어어어어억")
else:
	if mat >= 40:
		print("영어 점수 미달 불합겨어어어엉어ㅓ어어억")
	else: #이부분은 이미 총점에서 나가 떨어졌기 떄문에 필요가 없어욧!!
		print("영어, 수학점수 미달 불합겨어어어엉어ㅓ어어억")