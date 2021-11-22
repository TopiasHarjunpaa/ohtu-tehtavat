KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = max(kapasiteetti, 0)
        self.kasvatuskoko = max(kasvatuskoko, 0)
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)
                

    def poista(self, n):
        if self.kuuluu(n):
            self.alkioiden_lkm -= 1
            self.ljono.remove(n)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [alkio for alkio in self.ljono if alkio != 0]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        luvut = a.to_int_list() + b.to_int_list()
        
        for luku in luvut:
            x.lisaa(luku)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            if a in b_taulu:
                y.lisaa(a)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            if not a in b_taulu:
                z.lisaa(a)

        return z

    def __str__(self):
        tuotos = [alkio for alkio in self.ljono if alkio != 0]
        return str(tuotos).replace("[", "{").replace("]", "}")
