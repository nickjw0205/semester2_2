import random

# 배열을 보기좋게 출력
def print_array(s):
	print("[", end="")
	for i in s:
		if(i != s[len(s)-1]):
			print("%2.0d"%i, end=" ")
		else:
			print("%2.0d]"%i)

# 숫자를 저장할 배열을 선언
s = [0]*6

#몇번의 게임을 할건지 입력
input = int(input("몇번의 게임을 하시겠습니까?? : "))

# 게임을 시작합니다
print("로또 자동 %d게임 시작합니다." %input)

# input받은 만큼의 게임을 실행
for i in range(input):
	for j in range(6):					# 로또는 6개의 숫자를 뽑는다
		a = random.randrange(1,46)		# 랜덤한 숫자를 선택
		while(a in s):					# 중복된 수가 나오면 안되기에 중복이 되면 다시 뽑는다
			a = random.randrange(1,46)
		s[j] = a 						# 배열에 넣어준다
	print_array(s)						# 배열을 그냥 출력하면 찌그러지기때문에
										# 외부 함수로 배열 출력하는걸 선언

