pencil_price = 1000
pen_price = 2000

pencil_num = int(input("연필 몇개를 사시겠습니까???: \n"))
pen_num = int(input("펜 몇개를 사시겠습니까???: \n"))

total = (pencil_price * pencil_num) + (pen_price * pen_num)
discounted_price = total * 0.9

if total >= 10000:
	print("10000원이상 구매하셨으므로 10%를 할인해 드리겠습니다.")
	print("총 금액은 %d원 입니다." %discounted_price)

else:
	print("총 금액은 %d원 입니다." %total)