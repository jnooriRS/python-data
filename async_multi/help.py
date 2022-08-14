def fibArray(size):
    fibarray = [1, 1]
    while len(fibarray) < size:
        fibarray.append(sum(fibarray[-2:]))
    return fibarray

def fibwritefile(fibarray):
    for i in range(1, len(fibarray) + 1):
        with open(f"fib-number-{i}.txt", "w") as file:
            file.write("\n".join(map(str, fibarray[:i])))

fibarray=fibArray(7)
fibwritefile(fibarray)