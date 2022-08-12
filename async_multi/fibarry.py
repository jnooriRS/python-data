fibarray=[]
def fibArray(N):
    for X in range(N):
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
            continue
    print(fibarray)

fibArray(7)