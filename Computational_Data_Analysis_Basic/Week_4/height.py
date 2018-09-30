import time

def availablility_check(height, weight):
	if height >= 150 and weight >= 50:
		print("탑승 가능하십니다.")

	elif height >= 150 and weight < 50:
		print("죄송합니다. 몸무게 미달로 놀이기구를 탑승하실 수 없습니다.")

	elif height < 150 and weight >= 50:
		print("죄송합니다. 키 미달로 놀이기구를 탑승하실 수 없습니다.")

	else:
		print("죄송합니다. 키와 몸무게 미달로 놀이기구를 탑승하실 수 없습니다.")

def option_check(option):
	if option == "Yes":
		return 1
	elif option == "No":
		return 2
	else:
		return 3

print("놀이기구를 타기전에 탑승가능 여부를 판단하기위해 키와 몸무게를 측정하셔야하는데 괜찮으십니까?\n Yes / No ")
option = input()

if option_check(option == 1):
	height = int(input("키를 입력해주세요..."))
	weight = int(input("몸무게를 입력해주세요..."))
	print("\n조건을 충족하는지 확인중입니다...\n")
	time.sleep(1)
	availablility_check(height, weight)


elif option_check(option == 2):
	print("측정을 거부하셨습니다. 안녕히 가십시오.")

else:
	print("잘못입력하셨습니다. 저리가세요.")






