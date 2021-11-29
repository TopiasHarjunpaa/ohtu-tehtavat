class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulokset = []
        self.tulos = tulos
        self.tulokset.append(tulos)

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self.tulokset.append(self.tulos)

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self.tulokset.append(self.tulos)

    def nollaa(self):
        self.tulos = 0
        self.tulokset.append(self.tulos)

    def kumoa(self):
        if len(self.tulokset) > 1:
            self.tulokset.pop()
            self.tulos = self.tulokset.pop()
        else:
            self.tulos = 0
        self.tulokset.append(self.tulos)
        
    def aseta_arvo(self, arvo):
        self.tulos = arvo
        self.kumottu = False
