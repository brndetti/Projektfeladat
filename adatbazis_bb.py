import sqlite3

class ReceptAdatbazisBB:
    def __init__(self, fajlnev="receptek.db"):
        self.fajlnev = fajlnev
        self.table_letrehozasa()
    def kapcsolodas(self):
        return sqlite3.connect(self.fajlnev)

    def table_letrehozasa(self):
        with self.kapcsolodas() as kapcsolat:
            kapcsolat.execute(
                "CREATE TABLE IF NOT EXISTS receptek ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "nev TEXT NOT NULL,"
                "kategoria TEXT NOT NULL,"
                "ido INTEGER NOT NULL,"
                "hozzavalok TEXT NOT NULL)"
            )

    def receptek_listazasa(self, kereses=""):
        with self.kapcsolodas() as kapcsolat:
            kurzor = kapcsolat.cursor()
            kurzor.execute(
                "SELECT id, nev, kategoria, ido, hozzavalok "
                "FROM receptek WHERE nev LIKE ? ORDER BY nev",
                ("%" + kereses + "%",)
            )
            return kurzor.fetchall()

    def recept_mentese(self, nev, kategoria, ido, hozzavalok):
        with self.kapcsolodas() as kapcsolat:
            kapcsolat.execute(
                "INSERT INTO receptek (nev, kategoria, ido, hozzavalok) "
                "VALUES (?, ?, ?, ?)",
                (nev, kategoria, ido, hozzavalok)
            )

    def recept_modositasa(self, azonosito, nev, kategoria, ido, hozzavalok):
        with self.kapcsolodas() as kapcsolat:
            kapcsolat.execute(
                "UPDATE receptek SET nev=?, kategoria=?, ido=?,"
                "hozzavalok=? WHERE id=?",
                (nev, kategoria, ido, hozzavalok, azonosito)
            )

    def recept_torlese(self, azonosito):
        with self.kapcsolodas() as kapcsolat:
            kapcsolat.execute(
            "DELETE FROM receptek WHERE id=?", (azonosito,)
            )

def adatok_ellenorzese_bb(nev, kategoria, ido, hozzavalok):
    if not nev or not kategoria or not hozzavalok:
        return "Minden mezőt ki kell tölteni!"
    try:
        percek = int(ido)
    except ValueError:
        return "Az elkészítési idő egész szám legyen!"
    if percek < 0:
        return "Az elkészítési idő legyen pozitív!"
    if percek == 0:
        return "Az elkészítési idő nem lehet nulla!"
    return ""

