from random import randint


class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = 'Š'
        self.suviai = 0
        self.taskai = 100
        self.pataikymai = 0
        self.registras = {'Š': 0, 'P': 0, 'V': 0, 'R': 0}

    def pirmyn(self):
        self.kryptis = 'Š'
        self.y += 1
        self.taskai -= 10
        return self.y

    def atgal(self):
        self.kryptis = 'P'
        self.y -= 1
        self.taskai -= 10
        return self.y

    def kairen(self):
        self.kryptis = 'V'
        self.x -= 1
        self.taskai -= 10
        return self.x

    def desinen(self):
        self.kryptis = 'R'
        self.x += 1
        self.taskai -= 10
        return self.x

    def suvis(self):
        self.suviai += 1
        self.registras[self.kryptis] += 1
        return self.suviai, self.registras

    def info(self):
        print(f'Tanko padėtis x:{self.x} y:{self.y}, nusitaikyta {self.kryptis} kryptimi')
        print(f'Šūvių statistika: viso iššauta - {self.suviai}, pagal kryptis {self.registras}')
        print(f'Taškų likutis {self.taskai}, sunaikinta taikinių - {self.pataikymai}')

    def taikinys(self):
        self.prieso_x = randint(-10, 10)
        self.prieso_y = randint(-10, 10)
        return self.prieso_x, self.prieso_y

    def taikinio_ataka(self):
        if self.x == self.prieso_x:
            if self.prieso_y > self.y and self.kryptis == 'Š':
                return True
            if self.prieso_y < self.y and self.kryptis == 'P':
                return True
        if self.y == self.prieso_y:
            if self.prieso_x > self.x and self.kryptis == 'R':
                return True
            if self.prieso_x < self.x and self.kryptis == 'V':
                return True
        if self.x == self.prieso_x and self.y == self.prieso_y:
            print("Esi per arti taikinio, todėl ", end="")
            return False

    def pabaiga(self):
        if self.taskai < 0:
            print("Deja, baigėsi taškai - žaidimo pabaiga.")
            return 0


tankas = Tankas()
priesas = tankas.taikinys()

while True:
    if tankas.pabaiga() == 0:
        break
    print(f"Taikinio koordinatės x:{priesas[0]} y:{priesas[1]}")
    tankas.info()
    print()
    match (input('''"w" - važiuoti Šiaurės (Š) kryptimi,
"s" - važiuoti Pietų (P) kryptimi,
"a" - važiuoti Vakarų (V) kryptimi,
"d" - važiuoti Rytų (R) kryptimi,
"f" - ŠŪVIS!
"l" - baigti žaidimą.
Jūsų veiksmas:
''')):
        case 'w':
            tankas.pirmyn()
        case 'a':
            tankas.kairen()
        case 's':
            tankas.atgal()
        case 'd':
            tankas.desinen()
        case 'f':
            tankas.suvis()
            if tankas.taikinio_ataka():
                print("Pataikei! Sveikinu gauni 50 taškų!")
                print("Sekančio ", end="")
                tankas.pataikymai += 1
                tankas.taskai += 50
                priesas = tankas.taikinys()
            else:
                print("Nepataikei... Nusitaikyk iš naujo")
        case 'l':
            print("Žaidimo pabaiga")
            break
        case _:
            print("Klaidinga įvestis. Bandyk dar kartą!")
