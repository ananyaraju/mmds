dimension = input().split()
r = int(dimension[0])
c = int(dimension[1])

if (r!=c):
    print("only square matrices are valid\n")
else:
    m = []
    for x in range(r):
        val = input().split()
        print(val)
    print("\nmatrix: ")
    print(m)
