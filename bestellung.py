from daten import*
"""=================___Bestellprozess___================================"""
#Führt durch den Bestellprozess. Gibt eine Bestellung als Liste an den Warenkorb zurück.
def set_meal():     #"Margheritha", "Salami","4 Jahreszeiten"

    for i in s_set_meal:print(i) #Grafische Darstellung von set meal
    print(2*"\n")

    while True:
        bestellung=[]
        

        print("Aktuelle Speisekarte :",*speisekarte, sep=" , ",)
        print()

        user=input("Welche Pizza möchten sie ? Bitte händisch eintragen.\nSie können ihre Bestellung später ändern.\n>")
        print()

        if user in speisekarte:       #-------------------------------------------Wahl eines Gerichts
            print(f"Ihre Wahl : Pizza {user}")
            bestellung.append("Pizzasorte :")
            bestellung.append(user)

            bestellung.append(size())   #----------------------------------Wahl der Gerichtgröße

            add_extras: list[str | None] | None=specials(bestellung[2]) #-Wahl der Extra Zutaten
            bestellung.append(add_extras)

            bestellung.append(f"Zwischensumme in {EURO} :") #--------------Bildet Zwischensumme der laufenden Bestellung.
            bestellung.append(subtotal(bestellung))

            if debug_mode:
                print(bestellung)
                print(bestellung[-1])
            return bestellung

        else :
            print(f"Falsche Eingabe ! : {user}. Ihre Eingabe muss genau der Schreibweise auf der Speisekarte entsprechen.")


"""=================___size___================================"""

#Fragt nach der Größe des Gerichts.Größe ergibt den Basispreis.
def size() -> str:
    while True :
        user=input(f"Wählen sie eine Größe aus. Jede kleine Pizza kostet {i_klein}{EURO} Mittel kostet {i_mittel}{EURO} und Groß {i_groß}{EURO} .\nKlein (1), Mittel (2),Groß (3)>\n").strip()

        if user == "1":
            user=s_klein
            break

        elif user == "2":
            user=s_mittel
            break

        elif user == "3":
            user=s_groß
            break

        else :
            print(f"Eingabefehler ! Bitte Nochmal versuchen : Ihre Eingabe war :{user}. Erlaubt sind nur 1 oder 2 oder 3. Feststelltaste aktiviert?")
    return user

"""=================___Extras___================================"""

#bekommt die vorher ausgewählte größe des Gerichts.Interpretiert die größe als preis und bildet aus den extras und dem preis due Zwischensumme der aktuellen Bestellung.
def specials(groesse: str) -> list[str | None]:
    for i in s_specials:print(i) #Grafische Darstellung von specials
    print("\n")

    add_special:list[str|None]=["Extras :",]
    maximum:int=0
    speacials_counter:int=len(add_special) -1

    if groesse == s_klein:
        maximum:int=3
    elif groesse == s_mittel:
        maximum:int=4
    elif groesse == s_groß:
        maximum:int=5
    else:
        print("Falscher Parameter.Maximum auf 3.")
        maximum:int=3


    while True :
        
        
        if speacials_counter == maximum:
            print(f"Sie haben das derzeitige Maximum an Zutaten auf ihrer Pizza. {speacials_counter}/{maximum}.")
            print(*add_special, sep=",")
            print(f"Sie werden weiter geleitet...\n")
            break

        else:
            print("Verfügbare Extras:",*extras, sep=",")
            print()
            user:str=input(f"Aufgrund ihrer Größenauswahl können sie derzeit maximal {maximum} Zutaten hinzufügen.\n\nDrücken sie ENTER, um die Specials zu Überspringen.\nBitte Geben sie Ihre Extras nun händisch ein.\nSie haben aktuell {speacials_counter} Extras.\n>")

            if user == "" :
                print(f"Aktueller Bestellvorgang ist abgeschlossen.\n")

                break
            

            elif user in extras and speacials_counter != maximum : #Kann Extras als Zutat wählen. Muss noch ausgeschlossen werden TODO
                        add_special.append(user)
                        speacials_counter +=1

            elif speacials_counter == maximum:
                print(f"Das Maximum von derzeit {maximum} erreicht oder möchten die specials überspringen.\nSpecials :{speacials_counter}:{add_special}.\n")

            else:
                print(f"Ihre Eingabe existiert nicht in unserer Extra Liste. Bitte nochmal versuchen. Ihre Eingabe war : {user}")
                continue

    return add_special

#Interpretiert Größe zu einem int Wert und summiert die Anzahl der extras auf. 
def subtotal(bestellung) -> int | float:
    preis:int|float=0
    

    if bestellung[2] == s_klein :
        preis=i_klein # 5 Euro

    elif bestellung[2] == s_mittel :
        preis=i_mittel # 8 Euro

    elif bestellung[2] == s_groß:
        preis =i_groß # 12 Euro

    extra_zutaten:int|float=len(bestellung[3])-1 # bestellung[3] ist immer eine string liste .Sie beginnt stehts mit ["Extras :",] .
    zwischensumme:int|float=preis + extra_zutaten

    return zwischensumme
