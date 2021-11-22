from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostot = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for key, value in self.ostot.items():
            tavaroita += value.lukumaara()
        return tavaroita

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for key, value in self.ostot.items():
            hinta += value.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi not in self.ostot:
            ostos = Ostos(lisattava)
            self.ostot[lisattava.nimi] = ostos
        else:
            self.ostot[lisattava.nimi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi in self.ostot:
            self.ostot[poistettava.nimi].muuta_lukumaaraa(-1)
            if self.ostot[poistettava.nimi].lukumaara() == 0:
                del self.ostot[poistettava.nimi]
    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostoslista = []
        for key, value in self.ostot.items():
            ostoslista.append(value)
        return ostoslista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
