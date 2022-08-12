import os

#def fibwritefile(N):
 #   for X in range(1,N+1):
  #      with open(f"fib-number-{X}.txt", "w") as file:
   #         file.write(str(X))
    #        file.close()

#fibwritefile(10)
#for i in range(len(list_fruits)):


fibarray=[6,5,4,3,2,1]

def fibwritefile(fibarray):
    for X in range(len(fibarray)):
        with open(f"fib-number-{X}.txt", "w") as file:
            file.write(str(fibarray[X]))
            file.close()

fibwritefile(fibarray)