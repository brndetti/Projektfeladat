import tkinter as tk
from tkinter import ttk, messagebox

from adatbazis_bb import ReceptAdatbazisBB, adatok_ellenorzese_bb


class ReceptProgramBB:
    def __init__(self, root):
        self.root = root
        self.adatbazis_bb = ReceptAdatbazisBB()
        self.kivalasztott_id = None
        self.receptek=[]

        self.root.title("Receptgyűjtemény")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        ttk.Label(
            root, text="Receptgyűjtmény", font=("Arial", 17, "bold")
        ).grid(row=0, column=0, columnspan=4, pady=15)

        ttk.Label(root, text="Recept neve:").grid(
            row=1, column=0, sticky="w", padx=15, pady=5
        )
        self.nev = ttk.Entry(root, width=32)
        self.nev.grid(row=1, column=1, sticky="w", padx=5)

        ttk.Label(root, text="Kategória:").grid(
            row=2, column=0, sticky="w", padx=15, pady=5
        )
        self.kategoria = ttk.Combobox(
            root, values=["Leves", "Főétel", "Desszert", "Egyéb"],
            state="readonly", width=29,
        )
        self.kategoria.grid(row=2, column=1, sticky="w", padx=5)
        self.kategoria.set("Főétel")

        ttk.Label(root, text="Elkészítési idő (perc):").grid(
            row=3, column=0, sticky="w", padx=15, pady=5
        )
        self.ido = ttk.Entry(root, width=32)
        self.ido.grid(row=3, column=1, sticky="w", padx=5)

        ttk.Label(root, text="Hozzávalók és elkészítés:").grid(
            row=4, column=0, sticky="w", padx=15, pady=5
        )
        self.hozzavalok = tk.Text(root, width=45, height=5)
        self.hozzavalok.grid(row=4, column=1, columnspan=3, sticky="w", padx=5)

        ttk.Button(root, text="Új recept mentése", command=self.mentes).grid(
            row=5, column=0, padx=10, pady=12
        )

        ttk.Button(root, text="Módosítás", command=self.modositas).grid(
            row=5, column=1, padx=10, pady=12, sticky="w"
        )
        ttk.Button(root, text="Törlés", command=self.torles).grid(
            row=5, column=2, padx=10, pady=12
        )
        ttk.Button(root, text="Mezők ürítése", command=self.urites).grid(
            row=5, column=3, padx=10, pady=12
        )

        ttk.Label(root, text="Keresés név szerint:").grid(
            row=6, column=0, sticky="w", padx=15, pady=8
        )
        self.kereses = ttk.Entry(root, width=32)
        self.kereses.grid(row=6, column=1, sticky="w", pady=8)
        self.kereses.bind("<KeyRelease>", self.lista_frissitese)

        self.tabla = ttk.Treeview(
            root, columns=("id", "nev", "kategoria", "ido"),
            show="headings", height=10
        )
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nev", text="Recept neve")
        self.tabla.heading("kategoria", text="Kategória")
        self.tabla.heading("ido", text="Perc")
        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("nev", width=280)
        self.tabla.column("kategoria", width=180)
        self.tabla.column("ido", width=100, anchor="center")
        self.tabla.grid(row=7, column=0, columnspan=4, padx=15, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.recept_kivalasztasa)

        ttk.Button(root, text="Kilépés", command=root.destroy).grid(
            row=8, column=3, pady=10
        )
        self.lista_frissitese()

    def adatok(self):
        return(
            self.nev.get().strip(),
            self.kategoria.get().strip(),
            self.ido.get().strip(),
            self.hozzavalok.get("1.0", tk.END).strip(),
        )

    def adatok_helyesek(self):
        hiba = adatok_ellenorzese_bb(*self.adatok())
        if hiba:
            messagebox.showwarning("Hibás adat", hiba)
            return False
        return True

    def mentes(self):
        if not self.adatok_helyesek():
            return
        self.adatbazis_bb.recept_mentese(*self.adatok())
        self.urites()
        self.lista_frissitese()
        messagebox.showinfo("Siker", "A recept elmentve!")

    def modositas(self):
        if self.kivalasztott_id is None:
            messagebox.showwarning("Figyelem", "Válassz ki egy receptet!")
            return
        if not self.adatok_helyesek():
            return
        self.adatbazis_bb.recept_modositasa(
            self.kivalasztott_id, *self.adatok()
        )
        self.urites()
        self.lista_frissitese()
        messagebox.showinfo("Siker", "A recept módosítva!")

    def torles(self):
        if self.kivalasztott_id is None:
            messagebox.showwarning("Figelem", "Válassz ki egy receptet!")
            return
        if messagebox.askyesno("Megerősítés", "Biztosan törlöd a receptet?"):
            self.adatbazis_bb.recept_torlese(self.kivalasztott_id)
            self.urites()
            self.lista_frissitese()

    def urites(self):
        self.kivalasztott_id = None
        self.nev.delete(0, tk.END)
        self.kategoria.set("Főétel")
        self.ido.delete(0, tk.END)
        self.hozzavalok.delete("1.0", tk.END)
        for sor in self.tabla.selection():
            self.tabla.selection_remove(sor)

    def lista_frissitese(self, event=None):
        self.kivalasztott_id = None
        for sor in self.tabla.get_children():
            self.tabla.delete(sor)
        self.receptek = self.adatbazis_bb.receptek_listazasa(
            self.kereses.get().strip()
        )
        for recept in self.receptek:
            self.tabla.insert("", tk.END, values=recept[:4])

    def recept_kivalasztasa(self, event=None):
        kijeloles = self.tabla.selection()
        if not kijeloles:
            return
        adatok = self.tabla.item(kijeloles[0], "values")
        self.kivalasztott_id = int(adatok[0])
        for recept in self.receptek:
            if recept[0] == self.kivalasztott_id:
                self.nev.delete(0, tk.END)
                self.nev.insert(0, recept[1])
                self.kategoria.set(recept[2])
                self.ido.delete(0, tk.END)
                self.ido.insert(0, str(recept[3]))
                self.hozzavalok.delete("1.0", tk.END)
                self.hozzavalok.insert("1.0", recept[4])
                break


root = tk.Tk()
app = ReceptProgramBB(root)
root.mainloop()


