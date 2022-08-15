#import fibfunction
#create a folder
#single loop
#each iterable creates file
#iterable has a fib calucation
#result is saved as file name
#file pushed to folder
#IMPORT ALL MODULES INTO PROGRAMS WHEN FINISHED TO REFACTOR
import multiprocessing, time, os
from fibarry import fibArray, fibwritefile

def fibGenerator():
        path="C:\\Users\\HansPeterJonasHogh-J\\dev\\docs\\pyhtonexercise\\async_multi"
        os.chdir(path)
        fibFolder= 'fibFolder-01'
        os.makedirs(fibFolder)

def fibArray():
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

if __name__== "__main__":
    N = 7

    # singleprocessing
    st = time.time()
    fibGenerator(N)
    counter2(N)
    en = time.time()
    print("time taken = ", en-st)

    # multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=fibArray, args=(N, ))
    #p2 = multiprocessing.Process(target=counter2, args=(N, ))

    p1.start()
    #p2.start()

    p1.join()
    #p2.join()
    en = time.time()
    print("time taken = ", en-st)

#GITHUB for NERDZ multi programs
#https://github.com/Suji04/NormalizedNerd/blob/master/Python%20Tutorials/Multiprocessing/multi.py
