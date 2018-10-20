food = {"떡볶이" : "1000원",
		"짜장면" : "2000원",
		"라면"  : "1500원",
		"맥주"  : "3000원",
		"소주" : "4000원"}

# food.get("라면") #없어도 오류 X
# food["라면"] # 없으면 오류
# food.keys()
# food.values()

while(True):
	print()
	input_food = input(str(list(food.keys())) + "중 선택하세요: ")
	if(input_food in food):
		print("%s의 가격은 %s입니다." %(input_food, str(food.get(str(input_food)))))	
	else:
		print("그딴거 안팝니다.")

	



