from catclass import Cat, GoodCat, BadCat

print('good cats go')
Cat = GoodCat("Anthony")
Cat.meow()

print('bad cats go')
Cat = BadCat ("Asad")
Cat.meow()
