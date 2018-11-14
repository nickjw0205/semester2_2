def average(num1, num2):
	print((num1 + num2) / 2)


def average_return(num1, num2):
	return (num1 + num2) / 2	


def list_avg(list):
	total = 0
	for i in list:
		total += i
	return total/len(list)
	

def list_max(list):
	max = list[0]
	for i in list:
		if max < i:
			max = i
	return max


#가변 인풋
def fun1(*para):
	result = 0
	for i in para:
		result += i
	return result


def score():
	kor = int(input())
	eng = int(input())
	math = int(input())




list = [1,2,3,4,5,6]



