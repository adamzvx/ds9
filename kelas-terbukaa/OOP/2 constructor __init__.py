class Hero:
    # init dieksekusi saat init dibuat
    # __init__ / initialisiation / inisialisasi
    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        self.nama = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero('Dadang', 100, 5, 3)
hero2 = Hero('Micheal', 120, 8, 4)
hero3 = Hero('Irene', 200, 9, 1)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
