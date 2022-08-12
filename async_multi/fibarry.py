def fibArray(N):
    fibarray=[] 
    num1 = 0
    num2 = 1
    find = 2
    fibnum=0
    while find < N:
            fibnum = (num1+num2)
            num1 = num2
            num2 = fibnum
            find = (find+1)
            fibarray.append(int(fibnum))
    return(fibarray)

def fibwritefile(fibarray):
    for X in range(len(fibarray)):
        with open(f"fib-number-{fibarray[X]}.txt", "w") as file:
            file.write(str(fibarray[X]))
            file.close()

fibarray=fibArray(7)
fibwritefile(fibarray)