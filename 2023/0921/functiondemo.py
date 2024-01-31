#Call By Reference, mutable type
def change(target):
    target[0] = 10000
    print(f"안 = {target}")

original = [1,2,3]
print(f"전 = {original}")
change(original)
print(f"후 = {original}")