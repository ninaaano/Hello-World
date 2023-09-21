student = {}

def myinput(man) :
    name = input("이름 입력 : ")
    age = input("나이 : ")
    man["name"] = name
    man["age"] = age

myinput(student)
print(student)
