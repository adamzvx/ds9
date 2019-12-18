# class di deklarasikan sebelum main program/ program utama
class Hero:
    pass

# object/instance (instansiate)
hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Dadang'
hero1.health = 100

hero2.name = 'Ucup'
hero2.health = 100

hero3.name = 'Jhonson'
hero3.health = 200

print(hero1.__dict__)
print(hero1)
print(hero1.name)
