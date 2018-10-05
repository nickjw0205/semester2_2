
import random

answer_tuple = ("자! 이제 시작이야 내꿈은~",
		  "내꿈을 위한 여행 피카츄~",
		  "걱정따윈 없어, 없어~", 
		  "더이상 가사가 생각이 안나요",
		  "근데 더 치라고 하네요.",
		  "아직도 치라고요....?",
		  "몇개를 치시려고 하시는거에요...?",
		  "저 이제 힘들어요...")


Q = input("포케몬스터 노래를 볼까요?")
print("고민중.........\n"*4)

choice = random.randint(0,7)

print(answer_tuple[choice])

# if choice == 1:
# 	answer_print = answer_tuple[0]
# elif choice == 2:
# 	answer_print = answer_tuple[1]
# elif choice == 3:
# 	answer_print = answer_tuple[2]
# elif choice == 4:
# 	answer_print = answer_tuple[3]
# elif choice == 5:
# 	answer_print = answer_tuple[4]
# elif choice == 6:
# 	answer_print = answer_tuple[5]
# elif choice == 7:
# 	answer_print = answer_tuple[6]
# elif choice == 8:
# 	answer_print = answer_tuple[7]
# else:
# 	answer_print = "에러가 발생!!"

# print(answer_print)


