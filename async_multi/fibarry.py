def fibArray(N):
    fibarray=[1,] 
    num1 = 0
    num2 = 1
    find = 1
    fibnum=0
    while find < N:
            fibnum = (num1+num2)
            num1 = num2
            num2 = fibnum
            find = (find+1)
            fibarray.append(int(fibnum))
    return(fibarray)

def fibwritefile(fibarray):
    for X in range(1, len(fibarray) +1):
        with open(f"fib-number-{X}.txt", "w") as file:
            file.write(str(fibarray[:X]))
            file.close()

#use enumerate() for key value pair
#fibarray=fibArray(10000)
#fibwritefile(fibarray)