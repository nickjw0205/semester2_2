def change_channel_fun(now_channel, change_channel):
	return now_channel + change_channel

def change_volumn_fun(now_volumn, change_volumn):
	return now_volumn + change_volumn

now_channel = 0;
now_volumn = 0;

while(True):
	num = int(input("1. 채널		2. 음량		3. 종료"))
	if(num == 1):
		change_channel = int(input("바꾸고 싶은 만큼 입력"))
		now_channel = change_channel_fun(now_channel,change_channel)
		print("현재 채널 : %d\n" %(now_channel))

	elif(num == 2):
		change_volumn = int(input("바꾸고 싶은 만큼 입력"))
		now_volumn = change_volumn_fun(now_volumn,change_volumn)
		print("현재 채널 : %d\n" %(now_volumn))
	elif(num == 3):
		break

