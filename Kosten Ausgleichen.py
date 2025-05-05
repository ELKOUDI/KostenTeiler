# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import simpledialog, messagebox

def ausgleichen(zahlungen):
    gesamt = sum(zahlungen.values())
    anzahl_personen = len(zahlungen)
    durchschnitt = gesamt / anzahl_personen

    saldo = {}
    for person, betrag in zahlungen.items():
        saldo[person] = round(betrag - durchschnitt, 2)

    schuldner = {k: -v for k, v in saldo.items() if v < 0}
    glaeubiger = {k: v for k, v in saldo.items() if v > 0}

    transaktionen = []

    for schuldner_name, schuld_betrag in schuldner.items():
        for glaeubiger_name, glaeubiger_betrag in list(glaeubiger.items()):
            if schuld_betrag == 0:
                break
            zahlung = min(schuld_betrag, glaeubiger_betrag)
            transaktionen.append(f"{schuldner_name} zahlt {zahlung}? an {glaeubiger_name}")
            schuld_betrag -= zahlung
            glaeubiger[glaeubiger_name] -= zahlung
            if glaeubiger[glaeubiger_name] == 0:
                del glaeubiger[glaeubiger_name]

    return transaktionen

def start():
    try:
        anzahl = simpledialog.askinteger("Anzahl Personen", "Wie viele Personen seid ihr?")
        if anzahl is None:
            return

        zahlungen = {}
        for _ in range(anzahl):
            name = simpledialog.askstring("Name", "Name der Person:")
            betrag = simpledialog.askfloat("Betrag", f"Wieviel hat {name} bezahlt?")
            zahlungen[name] = betrag

        transaktionen = ausgleichen(zahlungen)

        if transaktionen:
            ergebnis = "\n".join(transaktionen)
        else:
            ergebnis = "Alles ist schon ausgeglichen!"

        messagebox.showinfo("Ausgleichszahlungen", ergebnis)

    except Exception as e:
        messagebox.showerror("Fehler", str(e))

# GUI-Fenster erstellen
root = tk.Tk()
root.title("Kosten Ausgleichen")
root.geometry("300x200")

button_start = tk.Button(root, text="Start", command=start, font=("Arial", 19))
button_start.pack(expand=True)

root.mainloop()
