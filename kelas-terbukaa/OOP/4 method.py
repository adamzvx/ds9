# class/ templaate di deklarassikan sebelum program
class Hero:
    # variabel class
    jumlahHero = 0

    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        self.nama = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1

    # void function, method tanpa return, tanpa argumen
    def intro(self):
        print('Halo.. saya bernama', self.nama)

    # method dengan argumen, tanpa agumen
    def tambahHealth(self, inputTambah):
        self.health += inputTambah
        print('Hmmm.. terima kasih telah peduli, kamu memberi darah', inputTambah)
        print('Darahku sekarang', self.health)

    #  method dengan return
    def cekHealth(self):
        return self.health

hero1 = input('halooo masukkan nama :')
hero1 = Hero(hero1, 100, 5, 3)
Hero.cekHealth(hero1)
Hero.tambahHealth(hero1, 10)
hero1.cekHealth()
hero1.tambahHealth(100)
