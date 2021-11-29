class Erotus:
    def __init__(self, sovellus, funktio):
        self.sovelluslogiikka = sovellus
        self.funktio = funktio
    
    def suorita(self):
        try:
            arvo = int(self.funktio())
        except Exception:
            arvo = 0        
        self.sovelluslogiikka.miinus(arvo)