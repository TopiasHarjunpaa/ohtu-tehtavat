from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class UI:
    def __init__(self, io):
        self.io = io
        
        self._komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

    def kaynnista(self):
        while True:
            self.io.valinta_ohje()
            valinta = self.io.lue()

            if valinta in self._komennot:
                self.io.peli_ohje()
                self._komennot[valinta].pelaa()
            else:
                break

