def fibArray(N):
    for X in range(N):
        fibarray=[]
        num1 = 0
        num2 = 1
        find = 2
        fibnum=0
        
        while find <= N:
            fibnum = (num1+num2)
            num1 = num2
            num2 = fibnum
            find = (find+1)
            fibarray.append(int(fibnum))
    print(fibarray)

@fibArray
def fibwritefile(fibarray):
    for X in (fibarray):
        with open(f"fib-number-{X.index}.txt", "w") as file:
            file.write(str(fibarray[X]))
            file.close()
            fibwritefile()

fibArray(7)