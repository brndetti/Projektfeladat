**Hallgató:** Brecska Bernadett - PATCXN  
**Tantárgy:** Szkript nyelvek - DUEL-ISR-116  
**Projekt:** Receptgyűjtemény  



## Feladat leírása

A program segítségével recepteket menthetünk el.
Egy új recept elmentéséhez szükséges megadnunk a recept nevét, kategóriáját, elkészítési idejét, illetve a hozzávalókat és az elkészítés lépéseit.
A már mentett receptek visszakereshetők, módosíthatók, illetve törölhetők is.

## A projekt fájljai

- `main.py` - program indítása, grafikus felület és eseménykezelés
- `adatbazis_bb.py` - saját modul (adatbáziskezelő osztály)
- `receptek.db` - automatikusan létrejövő adatbázis
- `ReadMe.md` - információs dokumentum

## Modulok és használt függvények

**Tanult modulok: `tkinter`**
- `tk.Tk()` - főablak létrehozása,
- `tk.Text()` - több soros szövegbevitel,
- `root.mainloop()` - eseménykezelő ciklus,
- `ttk.Label()`, `ttk.Entry()`, `ttk.Button()`, `ttk.Combobox()`, `ttk.Treeview()` - felületi elemek,
- `messagebox.showinfo()`, `showwarning()`, `askyesno()` - üzenetek.

**Bemutatandó modul: `sqlite3`**
- `sqlite3.connect()` - adatbázis-kapcsolat megnyitása,
- `kapcsolat.execute` - SQL utasítások végrehajtása,
- `kapcsolat.cursor` - kurzor létrehozása,
- `kurzor.execute` - lekérdezés indítása,
- `kurzor.fetchall` - a lekérdezés eredményeinek lekérése.
- `with` blokk - az adabázis-kapcsolat `with` blokkban működik, mely siker esetén menti, hiba esetén visszavonja a tranzakciót.

**Saját modul: `adatbazis_bb`**
- `ReceptAdatbazisBB` - saját adatbáziskezelő osztály,
- `adatok_ellenorzese_bb` - saját függvény, ellenőrzi a megadott adatokat.

## Osztályok

- `ReceptProgramBB` (`main.py`) - grafikus felület és gombok működése,
- `ReceptAdatbazisBB` (`adatbazis_bb.py`) - adatbázis létrehozása, olvasása és módosítása.

## Saját függvények és metódusok

- `adatok_ellenorzese_bb()` - adatellenőrzés,
- `tabla_letrehozasa()` - adatbázistábla elkészítése,
- `receptek_listazasa()` - keresés és listázás,
- `recept_mentese()` - új recept mentése,
- `recept_mododsitasa` - meglpvő recept módosítása,
- `recept_torlese()` - recept törlése,
- `mentes()`, `modositas()`, `torles()` - gombok műveletei,
- `lista_frissitese()`  - a táblazat frissítése,
- `recept_kivalasztasa()` - kiválasztott recept betöltése,
- `urites()` - beviteli mezők tartalmának törlése.

## Eseménykezelés
A gombok függvényeket hívnak meg a `command` paraméterrel.  
A keresőmező `<KeyRelease>` eseménye frissíti a találatokat.  
A táblázat `<<TreeviewSelect>>` eseménye betölti a kiválasztott receptet.  

## Program indítása

1. Python 3 telepítése szükséges, Tkinter támogatással. 
2. A `main.py` és az `adatbazis_bb.py` legyen ugyanabban a mappában.
3. A mappában futtassuk: `main.py`
4. A program az első indításor létrehozza a `receptek.db` fájlt.

Külső program telepítésére, illetve internetkapcsolatra a program futásához nincs szükség.

## Használat

1. Töltsd ki a recept adatait (név, kategória, elkészítési idő, hozzávalók és elkészítés), majd kattints az **Új recept mentése** gombra.
2. A keresőmezőbe irva szűrhetők a receptek.
3. Egy táblázatsorra kattintva az adatai megjelennek a mezőkben.
4. Adatok módosítás után kattints a **Módosítás** gombra.
5. A **Törlés** gomb törli a kiválasztott receptet, de csak a felhasználó megerősítése után.
6. A **Mezők ürítése** az egyes mezőkbe már beírt adatokat törli.