def Jadval_zarb():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    for i in range(0 , n+1):
        for j in range(0 , m+1):
            if i == 0 and j == 0:
                print("X", end = "\t")
            elif i == 0:
                print(j, end = "\t")
            elif j == 0:
                print(i, end = "\t")
            else:
                print(i * j, end = "\t")
            
    print()

Jadval_zarb()