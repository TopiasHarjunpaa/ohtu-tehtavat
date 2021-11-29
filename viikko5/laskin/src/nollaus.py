class Nollaus:
    def __init__(self, sovellus):
        self.sovelluslogiikka = sovellus
    
    def suorita(self):
        self.sovelluslogiikka.nollaa()