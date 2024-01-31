import copy

original = [1,2,3]
#target=original
target = copy.deepcopy(original)
print(original, target)
original[0] = 10000
print(original, target) #둘다바뀜