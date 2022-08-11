#import fibfunction
#create a folder
#single loop
#each iterable creates file
#iterable has a fib calucation
#result is saved as file name
#file pushed to folder

import multiprocessing
import  time

def fibGenerator(num):
     fibFolder = []
    for _ in range(num):
        #create file
        # fib calculation on itreable
        #assign iterable to file name
        #push file to folder
    print("counter1 done!")

def counter2(num):
    cnt = 0
    for _ in range(0, num, 2):
        cnt += 1
    print("counter2 done!")

if __name__ == "__main__":
    N = 1000

    # singleprocessing
    st = time.time()
    fibfile(N)
    counter2(N)
    en = time.time()
    print("time taken = ", en-st)

    # multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=counter1, args=(N, ))
    p2 = multiprocessing.Process(target=counter2, args=(N, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    en = time.time()
    print("time taken = ", en-st)