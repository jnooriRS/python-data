for i in range(1, 21):
    msg = "Your current value is"
    # print("Your current value is", i)
    if i % 3 == 0 and i % 4 == 0:
        print(f"{msg} FIZZBUZZ", i)
        continue
    if i % 3 == 0:
        print(f" {msg} fizz", i)
        continue
    if i % 4 == 0:
        print(f" {msg} buzz", i)
        continue
    print(msg, i)
