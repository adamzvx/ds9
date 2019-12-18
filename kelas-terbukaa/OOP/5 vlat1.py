class Hero:
    # variable class
    jumlahHero = 0

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlahHero += 1

    def serang(self, hero2):
        print('HaHaHa', self.name, 'telah menyerang', hero2.name)
        hero2.diserang(self, self.attack)
        # self diatas utk menunjuk hero1

    def diserang(self, hero1, hero1Attack):
        # self disini menunjukkan hero2
        hero1AttackNew = hero1Attack / self.armor
        print(self.name, 'diserang', hero1.name, 'dengan attack', hero1AttackNew)
        self.health -= hero1AttackNew
        print('Darah', self.name, 'adalah', self.health)

adam = Hero('adam', 100, 10, 5)
riki = Hero('riki', 100, 8, 7)

print(Hero.__dict__)
adam.serang(riki)
print('\n')
riki.serang(adam)
