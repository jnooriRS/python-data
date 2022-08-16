#IMPORT ALL MODULES INTO PROGRAMS WHEN FINISHED TO REFACTOR
import multiprocessing, time, os
def create_folder():
        path="C:\\Users\\HansPeterJonasHogh-J\\dev\\docs\\pyhtonexercise\\async_multi"
        os.chdir(path)
        fib_folder= 'fibFolder-01'
        os.makedirs(fib_folder)

def generate_array(fib_position):
    fibarray=[1,] 
    num1 = 0
    num2 = 1
    current_index = 1
    fibnum=0
    while current_index < fib_position:
            fibnum = (num1+num2)
            num1 = num2
            num2 = fibnum
            current_index = (current_index+1)
            fibarray.append(int(fibnum))
    return(fibarray)

def write_file(fibarray):
    for X in range(1, len(fibarray) +1):
        #https://www.pythontutorial.net/python-oop/python-enumeration/#:~:text=%20Python%20Enumeration%20%201%20Introduction%20to%20the,method%2C%20you%20can%20also%20use%20a...%20More%20
        #Use link to import enum- so fibarray.key and fibarray.value can be used instead
        with open(f"fib-number-{X}.txt", "w") as file:
            file.write(str(fibarray[:X]))
            file.close()

if __name__== "__main__":
    fib_position = 7

# multiprocessing
st = time.time()
#integer will not parse and be iterable without comma as it will be a tuple
#parse through integer
#p1 = multiprocessing.Process(target=fibGenerator)
p2 = multiprocessing.Process(target=generate_array, args=(fib_position, ))

#p1.start()
create_folder()
fibarray=generate_array(fib_position)
write_file(fibarray)
p2.start()

#p1.join()
p2.join()

st = time.time()
en = time.time()
print("time taken = ", en-st)

#GITHUB for NERDZ multi programs
#https://github.com/Suji04/NormalizedNerd/blob/master/Python%20Tutorials/Multiprocessing/multi.py
