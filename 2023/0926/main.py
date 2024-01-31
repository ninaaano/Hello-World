#pylint test
def myfunction(msg):
    # a = 0
    # b = 10
    msg_local = msg # 지역변수 = 파라미터변수
    def myfunction_inner(): 
        return msg_local
    return myfunction_inner

MSG = "hello,world".upper
aaa = myfunction(MSG)
print(aaa())
    