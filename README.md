
![Hauptmenü](Pizzarando_Hauptmenü.png)

# Pizzarando

Ein Pizza-Bestellsystem für die Konsole, geschrieben in Python.
Mein erstes größeres Lernprojekt.

## Funktionen

- Pizza wählen, Größe festlegen, Extras hinzufügen (Maximum je nach Größe)
- Warenkorb anzeigen, Bestellungen ändern oder löschen
- Checkout mit simulierter Zahlung (Demo, keine echte Zahlung)

## Starten

Voraussetzung: Python 3.10 oder neuer.

```bash
python main.py
```

Zum Ausprobieren des Checkouts: Passwort und Prüfziffer `1234,000`.

## Projektstruktur

| Datei | Aufgabe |
|---|---|
| `main.py` | Hauptmenü und Programmschleife |
| `bestellung.py` | Bestellprozess (Pizza, Größe, Extras, Zwischensumme) |
| `shoppingcart.py` | Warenkorb und Checkout |
| `daten.py` | Speisekarte, Preise, Grafiken |
| `utils.py` | Hilfsfunktionen |

## Was ich dabei gelernt habe

Aufteilung in Module, Probleme mit `import *`, Umgang mit veränderlichen Listen.
Eine Neuumsetzung mit Dict und Klassen ist geplant.

## Lizenz

MIT
