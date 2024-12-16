# Hirsipuu-peli

Yritys luoda yksinkertainen hirsipuu-peli.
Apuna on hydynnetty ChatGPT 

---

## **Ohjelman toiminta**

1. Ohjelma lukee sanat CSV-tiedostosta nimeltä `sanat.csv`. 
2. Peli valitsee satunnaisen sanan sanalistasta.
3. Pelaaja arvaa kirjaimia yksi kerrallaan:
   - Jos kirjain löytyy sanasta, se paljastetaan sanan oikeaan kohtaan.
   - Jokainen väärä arvaus vähentää pelaajan jäljellä olevia yrityksiä.
4. Pelin päättyessä ohjelma ilmoittaa voitosta tai häviöstä sekä näyttää oikean sanan.
5. Lopussa on mahdollisuus aloittaa uusi peli tai sulkea ohjelma

![image](https://github.com/user-attachments/assets/5b0c455d-6dcf-4546-830f-0a9984ed522c)


[Videoesittely](https://youtu.be/K1e69HCFvRA)

---

## **Ohjeet ohjelman suorittamiseen**

### **Asennus**
- Varmista, että tietokoneessasi on Python 3.7 (tai uudempi) asennettuna. [Linkki lataussivulle (aukeaa samalle välilehdelle)](https://www.python.org/downloads/) 
- Lataa tai kloonaa tämä projekti.
- sirry komentorivillä oikeaan kansioon
- Suorita kometorivillä:
  ```bash
  python hirsipuu.py

  
