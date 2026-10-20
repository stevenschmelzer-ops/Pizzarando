from daten import*
from bestellung import*
import time


"""=================___Hilfsfunktionen___================================"""
#übergebener integer ist countdown. 
def countdown(sekunden:int,printout:str) -> None:
    while sekunden > 0:
        # Formatiert Sekunden in MM:SS (Minuten:Sekunden)
        mins, secs = divmod(sekunden, 60)
        zeit_format = f"{mins:02d}:{secs:02d}"
        
        # Gibt die Zeit aus und überschreibt die aktuelle Zeile
        print(zeit_format, end="\r")
        
        time.sleep(1)
        sekunden -= 1
        
    print(printout)



def menu_print(objekt:list[str]) -> None:#Grafische Darstellung
    for i in objekt:print(i) 

