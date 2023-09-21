# born_year = int(input("Born Year : "))
# age = 2023 - born_year

# print("age = " + str(age))

address = "서울시 강남구 역삼동"

#인덱싱
print(address[0])
print(address[4])

# 슬라이싱
print(address[4:7])
print(address[0:3])

# + operator
print("hello" + "world" + "good") 

# * operator
print("Hello" * 3)

name = "mimi"
age = 24
print("name " + name + ", age " + str(age))
print("name is %s, age is %d" %(name,age))
print(f"name {name:10s}, age {age:5d}") #f없으면 적은대로 나옴 :뒤에 문자가 없으면 공백
