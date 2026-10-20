from daten import*
from bestellung import*
from shoppingcart import*
from utils import*

"""Projekt Aufteilung :

pizzarando/
├── main.py            # main(); while-Schleife: SIE SIND DERZEIT HIER
├── daten.py           # 
├── bestellung.py      # set_meal(), size(), specials(), subtotal()
├── warenkorb.py       #  shopping_cart(), show_cart_items(), update_car_item(), checkout)()
└── hilfen.py          # countdown(),menu_print(),debugging()

"""
"""=================___Hauptanwendung___================================"""



def main():     #"Programm Beenden (0)","Bestellvorgang starten (1)", "Speisekarte einsehen (2)", "Zum Warenkorb (3).
    
    menu_print(welcome)#Grafische Darstellung von welcome
    print("\n")
    print("Willkommen zu Pizzarando ! Wir kümmern uns um ihren Hunger. Was wünschen sie?\n")

    while True :
        menu_print(s_hauptmenü)
        user:str=input(f"\nWas möchten sie tun ? {s_main_menu[1]},{s_main_menu[2]}, {s_main_menu[3]}, {s_main_menu[0]}.\nBestätigen sie ihre Eingabe mit Enter.\n>") 

        if user == "0":
            print(s_main_menu[0])
            print("Warenkorb wird geleert...\n")
            warenkorb.clear()
            countdown(2,"Auf wiedersehen")
            break

        elif user == "1":
            warenkorb.append(set_meal())

        elif user == "2":
            welcome_mode=True
            print()
            menu_print(s_speisekarte)
            print("Speisekarte :",*speisekarte, sep=" , ")
            print()
            input("Weiter mit Enter.\n")

        elif user == "3":
            welcome_mode=True
            print(s_main_menu[3])
            shopping_cart()

        else:
            welcome_mode=True
            print(f"Unzulässige Eingabe. Bitte erneut versuchen. Ihre Eingabe : {user}")

if __name__ == "__main__":
    main()