greeting = "what age were you in when the London eye opened"
print(greeting)
age = int(input("How old are you: "))
name =str(input("What is you name: "))
print(f"To confirm we got it right you are {name}, and {age} years old.")

year_born = int(2022 - age)
age_at = int(1999 - year_born)
print(f"you were {age_at} when the London eye opened in 1999")
