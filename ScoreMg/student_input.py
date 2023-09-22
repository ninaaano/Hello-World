#input

def student_input(student) :
    name = input("name : ")
    kor = int(input("Korean : "))
    eng = int(input("English : "))
    math = int(input("Math : "))
    student["name"] = name
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math

    