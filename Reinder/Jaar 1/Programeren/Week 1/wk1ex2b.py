"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 0.5

    print("De queeste naar taart.")
    print()
    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten!")
    print()

#Tussen elk stuk is er een time.sleep(delay) toegevoegd om het makkelijker te laten lezen
    time.sleep(delay)

# In dit stuk wordt er gebruik gemaakt van 1 if 2 elifs en 1 else
    choice1 = input("Welke smaak zoekt u? ")
    if choice1 == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif choice1 == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    elif choice1 == "chocolade":
        print("Geweldige keus!")
    else:
        print("Ieder zijn smaak...")

    time.sleep(delay)

    print()
    choice2 = input("Wil je doorgaan? ")

# Hier wordt alleen maar gebruik gemaakt van 1 if en verder geen elif of else
    if choice2 == "ja":
        print("Je hebt gekozen om weg te gaan en komt uit bij een fontein. ")

    time.sleep(delay)

    print()
    choice3 = input("Je kan nu naar links of naar rechts waar wil je heen? ")

# Bij dit stuk is er 1 if en 1 elif en verder geen else
    if choice3 == "Links":
        print("Gooie keuze je ruikt de taart al!")
    elif choice3 == "Rechts":
        print("Je komt uit bij een grote kamer.")

    time.sleep(delay)

    print()
    choice4 = input("Je denkt dat je nog moet wachten op je taart ga je nu, over 1 uur of morgen pas? ")

# Hier is er 1 if 1 elif en 1 else
    if choice4 == "1 uur":
        print("Je gaat nu weg voor je taart.")
    elif choice4 == "nu":
        print("Je gaat direct weg voor je taart.")
    else:
        return "Je bent doodgegaan door de honger."

    print()
    print("Voorwaarts naar de queeste!\n\n")
    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")

    time.sleep(delay)

    print()
    choice5 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

# En hier is er 1 if geen elifs en 1 else
    if choice5 == "tafel":
        print("Als u de tafel benadert lijkt de onduidelijke massa")
        print("een steeds grotere vorm aan te nemen, tot ...")

        time.sleep(delay)

        print("... ze herkenbaar wordt als een grote stapel verpakte")
        print("taarten, het karton strak geplooid. Uw uitdaging --en")
        print("honger-- is op smakelijke wijze opgelost.")
        print()
        print("Tot ziens,", username, "!")
    else:
        print("U opent de deur en ziet een congregatie van wijze dames")
        print("en heren, die allen genieten van hun taken. Samenwerking")
        print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

        time.sleep(delay)

        print("...ze hebben ALLE taart opgegeten! Resten van dozen")
        print("liggen overal verspreid. U wordt duizelig en grijpt")
        print("naar een taart. Er is niets. U ademt uit en valt,")
        print("en ligt verslagen tussen de resten van dozen die u")
        print("langzaam bedekken tot verstikking volgt.")
        print()
        print("Vaarwel,", username, ".")