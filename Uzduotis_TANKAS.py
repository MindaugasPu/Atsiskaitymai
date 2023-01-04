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
        print(f'Tanko padėtis x:{self.x} y:{self.y}, kryptis į {self.kryptis} || Bendras šūvių skaičius:'
              f' {self.suviai} - {self.registras}')
        print(f'Taškų likutis {self.taskai}, pataikymai į priešą {self.pataikymai}')

    def taikinys(self):
        self.x2 = randint(-10, 10)
        self.y2 = randint(-10, 10)
        return self.x2, self.y2

    def taikinio_ataka(self):
        if self.x == self.x2:
            if self.y2 > self.y and self.kryptis == 'Š':
                return True
            if self.y2 < self.y and self.kryptis == 'P':
                return True
        if self.y == self.y2:
            if self.x2 > self.x and self.kryptis == 'R':
                return True
            if self.x2 < self.x and self.kryptis == 'V':
                return True
        if self.x == self.x2 and self.y == self.y2:
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

#commit testas 2
