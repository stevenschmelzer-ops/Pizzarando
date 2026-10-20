from daten import*
from utils import*
from bestellung import set_meal
import random

# shoppingcart.py


#Basis Datentyp . Auf der nachfolgenden Warenkorb Liste basiert die gesamte Anwendnung :
#[0|Pizza,  1 |Pizzasorte,     2|Größe=Preis,      3|  [   0|Extras :,   1|Zwiebeln,ect.],   4| Zwischensumme:,      5/-1 | 7]
"""=================___Warenkorb verändern___================================"""
#Submenü des main() . Aufgabenbereich :Warenkorb

def shopping_cart() -> None: 

    while True :
        if not warenkorb:
            menu_print(s_shopping_cart) #Grafische Darstellung
            print("\n")
            input("Ihr Warenkorb ist Leer !\nWeiter mit Enter .\n")
            break

        else:
            menu_print(s_shopping_cart)#Grafische Darstellung
            print("\n")
            user: str=input("Im folgenden können sie ihre Bestellung :  Anzeigen (1) ,Ändern (2) ,Checkout (3) ,Hauptmenü (0).\n>")
            print()

            if user == "1":
                show_cart_items()

            elif user == "2":
                update_cart_item()

            elif user == "3":
                checkout()

            elif user == "0":
                break

            else:
                print(f"Eingabefehler ! Bitte Nochmal versuchen : Ihre Eingabe war :{user}. Erlaubt sind nur 1 oder 2 oder 3.\n")

"""=================___Warenkorb Anzeigen___================================"""
#iteriert durch warenkorb und printet ihn aus .#gesamtsumme() implementiert
def show_cart_items() -> None:

    menu_print(s_show_cart_items) #Grafische Darstellung

    for zähler, bestellung in enumerate(warenkorb, start=1):
        print(f"Bestellung: {zähler}; ", *bestellung)
        print()
    gesamtsumme(warenkorb)
    input("Weiter mit Enter.")


"""=================___Warenkorb ändern___================================"""

#Menü zum Warenkorb abändern (Anzahl anpassen oder entfernen),Warenkorb ansehen,checkout
def update_cart_item() -> None:
    while True:
        if not warenkorb:
            print("Ihr Warenkorb ist leer.")
            break

        user: str = input("Warenkorb: Bestellung ändern (1), löschen (2), zurück (0).\n>").strip()

        if user == "1":
            index: int | None = bestellnummer_waehlen()
            if index is not None:
                print("Bisherige Bestellung :", *warenkorb[index])
                warenkorb[index] = set_meal()
                show_cart_items()

        elif user == "2":
            bestellung_loeschen()

        elif user == "0":
            break

        else:
            print(f"Eingabefehler ! Ihre Eingabe war : {user}. Erlaubt sind nur 0, 1 oder 2.")
#Fragt nach einer Bestellnummer. Gibt den Listenindex zurück, bei Abbruch oder Fehler None
def bestellnummer_waehlen() -> int | None: 

    show_cart_items()
    eingabe: str = input("Bestellnummer eingeben. Abbrechen mit Enter.\n>").strip()

    if eingabe == "":
        print("Abbruch.")
        return None

    if not eingabe.isdigit():   # lehnt Buchstaben und negative Zahlen ab
        print(f"Nur Zahlen sind erlaubt. Ihre Eingabe war : {eingabe}")
        return None

    nummer: int = int(eingabe)
    if 1 <= nummer <= len(warenkorb):
        return nummer - 1       # Anzeige beginnt bei 1, Liste bei 0

    print(f"Es gibt nur Bestellungen von 1 bis {len(warenkorb)}.")
    return None


def bestellung_loeschen() -> None:
    user: str = input("Löschen: Einzelne Bestellung (1), Warenkorb leeren (2), Abbrechen (0).\n>").strip()

    if user == "1":
        index: int | None = bestellnummer_waehlen()
        if index is not None:
            entfernt: list[str | list[str] | int | float | None] = warenkorb.pop(index)
            print("Entfernt :", *entfernt)

    elif user == "2":
        warenkorb.clear()
        print("Warenkorb geleert.")

    elif user == "0":
        print("Abbruch.")

    else:
        print(f"Eingabefehler ! Ihre Eingabe war : {user}. Erlaubt sind nur 0, 1 oder 2.")


"""=================___Bestellung bezahlen / abschließen___================================"""
# Bestellung ansehen ,payout ,else zurück zu update_cart

def checkout() -> None:
    menu_print(s_checkout)
    bezahlt: bool = False
    ankunft: int = random.randint(20, 40)
    while True:
        
        show_cart_items()

        user = input(
            f"Wie möchten Sie zahlen?\n"
            f"Verfügbare Zahlungsmittel: {', '.join(zahlungsmittel)}. "
            f"Bitte händisch eingeben:\n>"
        )

        if user in zahlungsmittel: # pw,pfz="1234,000"
            while True:
                pw = input(
                    "Bitte Passwort und Prüfziffer eingeben. "
                    "Trennen Sie Ihre Eingabe mit einem Komma.\nAbbruch mit ENTER .\n>"
                )

                if pw == pw_plus_pfz:
                    print("Verifizierung erfolgreich. Zahlung wird abgewickelt...Warenkorb wird geleert...")
                    print(f"Die Bestellung ist auf dem Weg zu ihnen ! geschätze Ankunft : {ankunft} minuten.")
                    countdown(3,"Weiterleitung zu shopping cart")
                    bezahlt = True
                    warenkorb.clear()
                    break

                elif pw == "":
                    print("Abbruch")
                    break

                else:
                    print(f"Inkorrekte Daten eingegeben! Ihre Eingabe war: {pw} .\nBei Problemen geben sie : 1234,000 ein ;-) .")

            if bezahlt:
                break

        elif user == "":
            print("Abbruch.")
            break

        else:
            print(
                "Eingabe fehlerhaft oder Zahlungsmittel nicht in unserer Liste. "
                f"Ihre Eingabe war: {user}."
            )

#toatal sum
def gesamtsumme(warenkorb)  -> int | float: #funktioniert nur mit dem Pizzarando List Warenkorb
    gesamtsumme = 0
    for item in warenkorb:
        preis: str | list[str] | int | float | None = item[-1]  # Greift auf das letzte Element (7) zu
        
        # Optional: Prüfen, ob es sich um eine Zahl handelt (int oder float)
        if isinstance(preis, (int, float)):
            gesamtsumme += preis
    print(f"Gesamtsumme: {gesamtsumme} €")  # Output: Gesamtsumme
    return gesamtsumme


