#main.py
import student_input
import student_calc
import student_output

print("programm is start")
student = {}
student_input.input(student) #student -> dict. call by reference
student_calc.calc(student)
student_output.output(student)

print("end")