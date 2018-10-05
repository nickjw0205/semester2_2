A_list = ["A","B","C"]

B_list = ["A", "B", "C", 1, 2]

C_list = A_list + B_list

D_list = [1,3,4,2,6,9,21,99]

D_list.sort()
# print(D_list)    #[1, 2, 3, 4, 6, 9, 21, 99]
# print(D_list.pop())		#99
D_list.insert(2,40)		#[1, 2, 10, 3, 4, 6, 9, 21, 99]
D_list.extend([10,20,30])		#[1, 2, 40, 3, 4, 6, 9, 21, 99, 10, 20, 30]

days = ("월", "화", "수", "목", "금", "토", "일") 		
# tuple은 수정이 불가능해욧!
print(days)

