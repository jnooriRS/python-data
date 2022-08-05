from catclass import Cat, GoodCat, BadCat, VeryBadCat

print('good cats go')
Cat = GoodCat("Anthony")
Cat.meow()

print('bad cats go')
Cat = BadCat ("Asad")
Cat.meow()

print('very bad cats need cages')
Cat = VeryBadCat('Jonas')
print(Cat.name)
Cat.meow()

Cat.meow()