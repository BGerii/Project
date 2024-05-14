from datetime import datetime


class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam  # Szoba osztály inicializálása: szobaszám és ár beállítása
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam,
                         10000)  # Egyágyas szoba inicializálása: szobaszám beállítása és ár 10000-re állítása


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam,
                         15000)  # Kétágyas szoba inicializálása: szobaszám beállítása és ár 15000-re állítása


class Szalloda:
    def __init__(self, nev):
        self.nev = nev  # Szálloda inicializálása: név beállítása
        self.szobak = []  # Szálloda szobáinak tárolására szolgáló lista inicializálása

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)  # Új szoba hozzáadása a szállodához


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba  # Foglalás inicializálása: szoba és dátum beállítása
        self.datum = datum


class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda  # Foglaláskezelő inicializálása: szálloda beállítása
        self.foglalasok = []  # Foglalások tárolására szolgáló lista inicializálása

    def foglalas(self, szobaszam, datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:  # Ellenőrzi, hogy a megadott szoba létezik-e a szállodában
                if not self.ellenoriz_foglalast(szoba,
                                                datum):  # Ellenőrzi, hogy a megadott szoba és dátumhoz van-e már foglalás
                    return None
                foglalas = Foglalas(szoba, datum)  # Foglalás létrehozása
                self.foglalasok.append(foglalas)  # Foglalás hozzáadása a foglalások listájához
                return szoba.ar  # Visszatér az adott szoba árával
        return None

    def lemondas(self, foglalas_sorszam):
        foglalas_index = foglalas_sorszam - 1
        if 0 <= foglalas_index < len(self.foglalasok):  # Ellenőrzi, hogy a foglalás sorszáma érvényes-e
            foglalas = self.foglalasok[foglalas_index]
            self.foglalasok.remove(foglalas)  # Foglalás törlése a foglalások listájából
            print("A foglalás sikeresen törölve.")
        else:
            print("Érvénytelen foglalás sorszám.")

    def listaz_foglalasok(self):
        for i, foglalas in enumerate(self.foglalasok):  # Foglalások listázása sorszámmal
            print(f"Foglalás {i + 1}: Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")

    def ellenoriz_foglalast(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum.date() == datum.date():  # Ellenőrzi, hogy egy adott szobára és dátumra már van-e foglalás
                return False
        return True


def adatok_feltoltese():
    szalloda = Szalloda("Példa Szálloda")  # Szálloda inicializálása
    szalloda.uj_szoba(EgyagyasSzoba("101"))  # Egyágyas szobák hozzáadása a szállodához
    szalloda.uj_szoba(KetagyasSzoba("201"))  # Kétágyas szobák hozzáadása a szállodához
    szalloda.uj_szoba(KetagyasSzoba("202"))  # Kétágyas szobák hozzáadása a szállodához
    return szalloda


def main():
    szalloda = adatok_feltoltese()  # Szálloda létrehozása és szobák hozzáadása
    foglalas_kezelo = FoglalasKezelo(szalloda)  # Foglaláskezelő létrehozása

    foglalas_kezelo.foglalas("101", datetime(2024, 5, 15))  # Példa foglalások létrehozása
    foglalas_kezelo.foglalas("201", datetime(2024, 5, 17))  # Példa foglalások létrehozása
    foglalas_kezelo.foglalas("202", datetime(2024, 5, 19))  # Példa foglalások létrehozása
    foglalas_kezelo.foglalas("101", datetime(2024, 5, 20))  # Példa foglalások létrehozása
    foglalas_kezelo.foglalas("202", datetime(2024, 5, 21))  # Példa foglalások létrehozása

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")

