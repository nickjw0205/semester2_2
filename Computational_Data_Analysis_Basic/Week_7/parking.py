parking = []
carname = "A"

while(True):

	select = int(input("1. 자동차 넣기  2. 자동차 뺴기 3. 끝 : "))
	if(select == 1):
		if(len(parking) >= 5):
			print("주차장에 차가 꽉차서 안돼. 저리가")
		else:
			parking.append(carname)
			print("%s 자동차 들어감. 상태 => %s \n" %(carname, parking))
			carname = chr(ord(carname) + 1)
	elif(select == 2):
		if(len(parking) <= 0):
			print("뺼 차가 없잖아 멍청아")
		else:
			outcar = parking.pop()
			print("%s 자동차 나감. 상태 => %s \n" %(outcar, parking))
			carname = chr(ord(carname) - 1)

	elif(select == 3):
		break

	else:
		print("잘못입력")