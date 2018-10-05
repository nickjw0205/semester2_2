a = tuple("hello")

s1 = [1, 2, 3, 4, 5]
s2 = [6, 7, 8, 9, 10]

student = {"학과": "소프트", "이름":"서지원", "학번": 1000}

student["연락처"] = "012345678"  # 연락처 목록 추가하기

student["학과"] = "변경을 해봅시다!" # 학과 바꾸기

student.get("이름") -> 오류 안남 없어도

student["이름"] -> 없을경우 오류남.

student.values() #dict_values(['변경을 해봅시다!', '서지원', 1000, '012345678'])

1000 in student.values(). # True


