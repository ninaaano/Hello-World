first = int(input("Enter a first number : "))
second = int(input("Enter a second number : "))

try :  
    print(f"{first} / {second} = {first/second}")
except Exception as err: 
    print(err)
finally : 
    print("Program is Over..")
# else : #정상적으로 처리가 끝나야 발생
#     print("Program is Over")