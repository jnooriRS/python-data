def fibArray(N):
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

fibArray(7)