import time

input("Enter키를 누르고 10초를 셉니다.")

start = time.time()

input("누르기")
end = time.time()

print("당신이 누른 시간은 ",abs(end - start), " 입니다.")