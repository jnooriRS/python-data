from catclass import Cat, GoodCat, BadCat, VeryBadCat, MyException
try:
        
    print('good cats go')
    cat = GoodCat("Anthony")
    cat.meow()

    print('bad cats go')
    cat = BadCat ("Asad")
    cat.meow()

    print('very bad cats need cages')
    cat = VeryBadCat('Jonas')
    print(cat.name)
    cat.meow()

except MyException as e:
    print(f"My error message is {e.message}")

except Exception as error:
    print("error is" + str(error))
 
#print(help(VeryBadCat))
#show what has been inheretied from the parent class
#snakecase