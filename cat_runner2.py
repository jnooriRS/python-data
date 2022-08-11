from catclass import Cat, GoodCat, BadCat, VeryBadCat

print('very bad cats need cages')
cat1: Cat = GoodCat("Jonas")
cat2: Cat = BadCat ("Anthony")
cat3: Cat = VeryBadCat("Asad")

def cat_cage(func):
    def inside():
        try:
            raise Exception (cat3.meow())
        except Exception as error:
                print (f"Cat was bad:{error}, no harm was done due to Cage")
        func()
    return inside

@cat_cage
def run_in_cage ():
    cat1.meow()
    cat2.meow()
    cat3.meow()
run_in_cage()