import random
import csv

def piirra_hirsipuu(yritykset):
    kuvat = [
        """
           
               

        _________
        """,
        """
           
           
         
               

        =========
        """,
        """
           
               

               |
               |
               |
        =========
        """,
        """
               +
               |
               |
               |
               |
        =========
        """,
        """
           +---+
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,
    ]
    print(kuvat[6 - yritykset])

def lue_sanat_csv_tiedostosta(tiedostonimi):
    sanat = []
    with open(tiedostonimi, mode='r', encoding='utf-8') as tiedosto:
        csv_lukija = csv.reader(tiedosto)
        for rivi in csv_lukija:
            sanat.extend(rivi) 
    return sanat

def hirsipuu():
    tiedostonimi = "sanat.csv"  # Käytetään oletuksena sanat.csv tiedostoa

    # Luetaan sanat CSV-tiedostostat
    sanat = lue_sanat_csv_tiedostosta(tiedostonimi)

    sana = random.choice(sanat)  # Arvotaan sana
    arvatut_kirjaimet = []  # Lista arvatuista kirjaimista
    yritykset = 6  # Pelaajan käytettävissä olevat yritykset

    while yritykset > 0:
        # Näytetään sanan tila
        piilotettu_sana = "".join([ 
            kirjain if kirjain in arvatut_kirjaimet else "_" 
            for kirjain in sana
        ])
        print(f"Sana: {piilotettu_sana}")
        print(f"Arvatut kirjaimet: {', '.join(arvatut_kirjaimet)}")  # Näytetään arvattujen kirjainten lista samalla rivillä
        piirra_hirsipuu(yritykset)

        # Tarkistetaan voitto
        if "_" not in piilotettu_sana:
            print(f"Onneksi olkoon! Arvasit sanan oikein: {sana}")
            break

        # Pyydetään pelaajalta kirjain
        arvaus = input("Arvaa kirjain: ").lower()

        # Tarkistetaan syötteen kelpoisuus
        if len(arvaus) != 1 or not arvaus.isalpha():
            print("Syötä vain yksi kirjain!")
            continue

        # Tarkistetaan, onko kirjain jo arvattu
        if arvaus in arvatut_kirjaimet:
            print("Olet jo arvannut tämän kirjaimen!")
            continue

        # Lisätään kirjain arvattuihin
        arvatut_kirjaimet.append(arvaus)

        # Tarkistetaan, onko kirjain sanassa
        if arvaus in sana:
            print(f"Hienoa! Kirjain '{arvaus}' on sanassa. Yrityksiä jäljellä: {yritykset}")
        else:
            yritykset -= 1
            print(f"Väärin! Kirjain '{arvaus}' ei ole sanassa. Yrityksiä jäljellä: {yritykset}")

    else:
        piirra_hirsipuu(0)
        print(f"Hävisit! Sana oli: {sana}")
    
    # Kysytään pelaajalta, haluaako hän pelata uudestaan
    uusi_peli = input("Haluatko pelata uudestaan? (y/n): ").lower()
    if uusi_peli == "y":
        hirsipuu()  # Aloitetaan uusi peli
    else:
        print("Kiitos pelaamisesta!")

if __name__ == "__main__":
    hirsipuu()
