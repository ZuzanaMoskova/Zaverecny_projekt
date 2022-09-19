#!/usr/bin/env python3

from pojistenec import Pojistenec

print("-------------------------")
print("Evidence pojistenych")
print("-------------------------")

class Evidence:
# trieda reprezentuje celkovú evidenciu poistených

    pole = []

    def vypis_moznosti(self):
    #vrátí výpis možností


        print("1 - Pridat nového pojisteného")
        print("2 - Vypsat všechny pojistené")
        print("3 - Vyhledat pojisteného")
        print("4 - Konec")

    def moznost(self):
    # uživatel zadáva číslo možnosti operácie
        cislo_operace = int(input("Zadejte číslo operace:\n"))
        return cislo_operace


    def vykonej_operaci(self,cislo_operace):
    #Vykoná príslušnú operáciu

        if cislo_operace == 1:
        # pri operácií číslo 1,uživatel zakladá svoje osobné údaje, ktoré sa pridajú do pole.
            jmeno = str(input("Zadejte jméno pojisteného:\n"))
            prijmeni = str(input("Zadejte příjmení:\n"))
            telefon = int(input("Zadejte telefonní číslo:\n"))
            vek = str(input("Zadejte vek:\n"))

            pojistenec = Pojistenec(jmeno,prijmeni,telefon,vek) # vytvoríme poistenca
            Evidence.pole.append(pojistenec)
            print(Evidence.pole)

            print("Data byla uložena.")

        elif cislo_operace == 2:
        # pri operácií číšlo 2 cyklus prechádza pole a printuje každého jedného poisteného, ktorý bol zadaný.
            for pojistenec in Evidence.pole:
                print(pojistenec)

        elif cislo_operace == 3:
        # pri operácií číslo 3 program vyhladáva poistených na základe vstupu zadaného mena a priezviska od uživatela.
        #program pomocou cyklu prechádza pole s uloženými datami z operácie číslo jedna,keď nastane zhoda, data sa vyprintujú.
        #ak sa požadovaný poistenec nenachádza v poli, program vypíše hlášku, že zadaný poistenec neexistuje.

            zadany_jmeno = str(input("Zadejte jméno pojisteného:\n"))

            zadany_prijmeni = str(input("Zadejte příjmení:\n"))

            for pojistenec in Evidence.pole:
                if zadany_jmeno == pojistenec.jmeno and zadany_prijmeni == pojistenec.prijmeni:
                    print(pojistenec)
                    break
                else:
                    print("Zadané jméno neexistuje.")


        elif cislo_operace >= 4:
        # pri zadaní možnosti operácie číšlo štyri sa program ukončí hláškou "Konec", neopakuje sa hláška, či chceme pokračovať.
            print("Konec")




