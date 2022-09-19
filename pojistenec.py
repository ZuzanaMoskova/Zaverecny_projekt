#!/usr/bin/env python3

class Pojistenec:
# trieda reprezentuje poistenca

    def __init__(self,jmeno,prijmeni,telefon,vek):
    # konstruktor
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

    def __str__(self):
    # textová reprezentace Pojistence
        return f"{self.jmeno}\t{self.prijmeni}\t\t{self.vek}\t\t{self.telefon}"

