import os

def fibwritefile(N):
    for X in range(1,N+1):
        with open(f"fib-number-{X}.txt", "w") as file:
            file.write(str(X))
            file.close()

fibwritefile(10)