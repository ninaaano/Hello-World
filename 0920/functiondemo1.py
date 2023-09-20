def calc_sum(start, end) : #파라미터, 매개변수
    sum = 0
    for i in range(start,end+1) :
        sum += i
    return sum
#함수의 끝

start = 50
end = 100
result = calc_sum(start,end) #인자, 아규먼트, Call by Value
print("%d 부터 %d까지의 합은 %d" % (start, end, result))
# print("%d 부터 %d 까지의 합은 %d" % (start, end, calc_sum(start,end)))