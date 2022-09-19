#!/usr/bin/env python3

from evidence import Evidence

evidence = Evidence() # vytvoríme evidenciu
pokracovat = "ano"


while pokracovat == "ano":

    evidence.vypis_moznosti() # voláme zoznam - výpis možností operácií
    moznost = evidence.moznost() # uživatel zadáva číslo operácie
    print(moznost)
    evidence.vykonej_operaci(moznost) # daná operácia sa vykoná

    if moznost == 4:
        pokracovat = "ne"
        break # cyklus lámeme u možnosti číslo 4 - Konec, kedy chceme, aby sa dalej neobjavovala hláška, či si prajeme pokračovat vo výberu možností
    else:
        pokracovat = input("Prejete si pokračovat ano/ne:\n")