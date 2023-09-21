student = {} #딕셔너리 선언
student["name"] = "mimi"
student["age"] = 24
student["address"] = "서울시 강남구 역삼동"
print(student) #{'name': 'mimi', 'age': 24, 'address': '서울시 강남구 역삼동'}
print(f"address is {student['address']}")

tuple_ = ("banana", 50, 89.5, True) # 괄호 생략 가능. tuple은 예약어지만 _ 넣으면 다른 이름이라 사용 가능
tuple_[3] = False # error. tuple은 수정할 수 없다
print(tuple_ * 3) # 더하기도 가능
