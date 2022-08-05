import sys
fib_postion=(int(sys.argv[1]))
#print(User)
def fib(fib_postior):
    fib1=0
    fib2=1
    current=0
    fibnum=0
    print(f"you want to find {fib_postion}?")
    while current < fib_postion:
        fibnum= fib1 + fib2
        fib1=fib2
        fib2= fibnum
        current+=1

    print(f"This is your number {fibnum}")
    return fibnum

fib(fib_postion)