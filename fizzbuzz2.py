import sys
#print(int, sys.argv[1:])
print (sys.version)

for i in range(int(sys.argv[1])):
    msg = "Your current value is"
    #print("Your current value is", i)
    if i %(int(sys.argv[2])) == 0 and i %(int(sys.argv[3])) == 0:
        print(f"{msg} FIZZBUZZ", i)
        continue
    if i %(int(sys.argv[2])) == 0:
     print( f" {msg} fizz", i)
     continue
    if i %(int(sys.argv[3])) == 0:
     print(f" {msg} buzz", i)
     continue
    print(msg, i)