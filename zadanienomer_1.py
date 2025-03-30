class Blyudo:
    def __init__(self, nazvanie, tsena, vremya_prigotovleniya):
        self.nazvanie = nazvanie
        self.tsena = tsena
        self.vremya_prigotovleniya = vremya_prigotovleniya

class Menu:
    def __init__(self):
        self.blyuda = []
    def dobavit_blyudo(self, blyudo):
        self.blyuda.append(blyudo)
    def ubrat_blyudo(self, nazvanie):
        self.blyuda = [blyudo for blyudo in self.blyuda if blyudo.nazvanie != nazvanie]

class Zakaz:
    def __init__(self, blyuda):
        self.blyuda = blyuda

class Restoran:
    def __init__(self, nazvanie):
        self.nazvanie = nazvanie
        self.menu = Menu()
    def dobavit_blyudo_v_menu(self, blyudo):
        self.menu.dobavit_blyudo(blyudo)
    def ubrat_blyudo_iz_menu(self, nazvanie):
        self.menu.ubrat_blyudo(nazvanie)
    def sozdat_zakaz(self, spisok_blyud):
        return Zakaz(spisok_blyud)
    def poschitat_itog_zakaza(self, zakaz):
        return sum(blyudo.tsena for blyudo in zakaz.blyuda)

restoran = Restoran("Vkusno i Tochka")
blyudo1 = Blyudo("Pizza", 500, 30)
blyudo2 = Blyudo("Pasta", 400, 20)

restoran.dobavit_blyudo_v_menu(blyudo1)
restoran.dobavit_blyudo_v_menu(blyudo2)

zakaz = restoran.sozdat_zakaz([blyudo1, blyudo2])
itog = restoran.poschitat_itog_zakaza(zakaz)
print(f"Summa zakaza: {itog} rub.")
