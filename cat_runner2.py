from catclass import Cat, GoodCat, BadCat, VeryBadCat

           
def cat_cage(func):
    def inside():
        try:
            func()
        except Exception:
            print (f"Cat was bad no haarm was done due to cage")
    return inside


@cat_cage
def run_in_cage():
    cat1.meow()
    cat2.meow()
    cat3.meow()


# Running.....
print('very bad cats need cages')
cat1: Cat = GoodCat("Jonas")
cat2: Cat = BadCat ("Anthony")
cat3: Cat = VeryBadCat("Asad")

run_in_cage()


#print as it first exectuable command
#cat1-cat3 are all functions to be passed into def inside- which has a try/except block
#for each function it will print out its respective meow
#except for verybadcat (hiss) as this raises an exception
#we now print out a new statement
#QUESTION - run_in_cage why does it not contain 3 arguments (1,2,3) 1 = cat1.meow() etc