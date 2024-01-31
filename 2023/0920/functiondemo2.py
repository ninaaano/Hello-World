# original = 5
# target = original
# print("origin = %d, target = %d" % (original, target))
# original = 10 #target 결과가 안바뀌었다?! 둘은 전혀 연결되어 있지 않기 때문이다
# print("origin = %d, target = %d" % (original, target))

def change(target) :
    target = 100
    print("target = %d" % target)
original = 5
print("전 : %d" % original)
change(original)
print("후 : %d" % original)