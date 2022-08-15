#import fibfunction
#create a folder
#single loop
#each iterable creates file
#iterable has a fib calucation
#result is saved as file name
#file pushed to folder
#IMPORT ALL MODULES INTO PROGRAMS WHEN FINISHED TO REFACTOR

from ast import Num
import multiprocessing, time, os
from fibarry import fibArray, fibwritefile

def fibGenerator():
        path="C:\\Users\\HansPeterJonasHogh-J\\dev\\docs\\pyhtonexercise\\async_multi"
        os.chdir(path)
        fibFolder= 'fibFolder-01'
        os.makedirs(fibFolder)

fibarray=fibArray(N)
fibwritefile(fibarray)


def counter2(num):
    cnt = 0
    for _ in range(0, num, 2):
        cnt += 1
    print("counter2 done!")

if __name__ == "__main__":
    N = 10000

    # singleprocessing
    st = time.time()
    fibGenerator(N)
    counter2(N)
    en = time.time()
    print("time taken = ", en-st)

    # multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=fibGenerator, args=(N, ))
    p2 = multiprocessing.Process(target=counter2, args=(N, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    en = time.time()
    print("time taken = ", en-st)

#GITHUB for NERDZ multi programs
#https://github.com/Suji04/NormalizedNerd/blob/master/Python%20Tutorials/Multiprocessing/multi.py
