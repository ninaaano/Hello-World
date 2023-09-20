count, line = 0, 1
for i in range(65,91):
    if line % 2 == 1 : 
        print(chr(i), end = '\t')
    else : print(chr(i + 32), end = '\t')
    count += 1
    if count % 5 == 0 : 
        print()
        line += 1
print()