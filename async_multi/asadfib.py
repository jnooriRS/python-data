def fibonacci(user_input):
    num1 = 0
    num2 = 1
    find = 2
    fibnum=0
    
    while find <= (int(user_input)):
        fibnum = (num1+num2)
        num1 = num2
        num2 = fibnum
        find = (find+1)
        continue
    return fibnum
        

user_input = input("Enter a number: ")
fibnum = fibonacci(user_input)
print (fibnum)


with open("fib-number.txt", "w") as file:
    file.write(str(fibnum))












