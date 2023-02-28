r1=int(input("Number of rows in matrix-1: "))
c1=int(input("Number of cols in matrix-1: "))
r2=int(input("Number of rows in matrix-2: "))
c2=int(input("Number of cols in matrix-2: "))

if (c1!=r2):
    print("matrix multiplication not possible")

else:
    m1=[]
    m2=[]

    print("\nenter matrix-1 data")
    for x in range(r1):
        col1=[]
        for y in range(c1):
            val=int(input("data: "))
            col1.append(val)
        m1.append(col1)
    print("matrix-1: ")
    print(m1)

    print("\nenter matrix-2 data")
    for x in range(r2):
        col2=[]
        for y in range(c2):
            val=int(input("data: "))
            col2.append(val)
        m2.append(col2)
    print("matrix-2: ")
    print(m2)
        
    result=[]
    sum=0
    print("\nmultiplication: ")
    for i in range(r1):
        for j in range(c1):
            for k in range(r2):
                sum=sum+(m1[i][k]*m2[k][j])
            print(sum, end="  ")
            sum=0
        print()