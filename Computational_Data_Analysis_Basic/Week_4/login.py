# ----------입력받아 가입---------------

# input_id = input("id를 입력해주세요....:")
# input_pw = input("pw를 입력해주세요....:")

# if len(input_id) < 10:
# 	if len(input_pw) < 10:
# 		print("회원가입 완료!")
# 	else:
# 		print("비밀번호가 너무 길어요ㅠㅠ 가입 실패!!")
# else:
# 	print("아이디가 너무 길어요ㅠㅠ 가입 실패!!")

#-----------로그인----------------

original_id = "abcd"
original_pw = 1234

input_id = input("id를 입력해주세요....:")
input_pw = int(input("pw를 입력해주세요....:"))

if original_id != input_id:
	print("실패! 아이디가 다릅니다!!")
else:
	if original_pw != input_pw:
		print("실패! PW가 다릅니다!!")
	else:
		print("로그인 성공!")