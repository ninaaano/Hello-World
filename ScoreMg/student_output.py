def output(student) : 
    print(f"{student['name']}\t{student['kor']}\t{student['eng']}",end='\t')
    print(f"{student['math']}\t{student['totla']}\t{student['avg']:.2f}", end='\t')
    print(f"{student['grade']}")