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
    delay = 0.7

    print ("De taart queeste.")
    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten!")
    print()

    flavor = input("Welke smaak zoekt u? ")
    if flavor == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif flavor == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    elif flavor == "appel":
        print("Appel? Wat een geweldige keuze!")
    else:
        print("Ieder zijn smaak...")

    print()
    print("Vervolgends gaat u verder in het labyrint en komt een T-splitsing tegen waar u links of rechts kan gaan")
    print()

    choice2 = input("Wilt u links of rechts?")
    if choice2 == "links":
        print("Wat een geweldige keuze!")
    elif choice2 == "rechts":
        print("Ik zou geen betere keuze kunnen bedenken!")

    time.sleep(delay)

    print()
    choice3 = input("Wil je doorgaan met het Avontuur?")
    if choice3 == "Ja":
        print("Goed gekozen avonturier, Wij gaan samen verder op zoek naar de beste taart in het rijk!")

    time.sleep(delay)

    print()
    print("U krijgt twee de mogelijkheden.")
    print("Er bevinden zich 2 doorgangen:")
    print("De eerste doorgang staan u vele rijkdommen en mooie vrouwen te wachten.")
    print("De tweede doorgang staat u Kapitein Haak op te wachten om met u te vechten")
    print("om de grote staf der 7 zeeën.")
    print()
    
    choice1 = input("Wat is uw keuze? doorgang een of doorgang twee?")
    if choice1 == "doorgang een":
        print("Een goede keuze voor een wijze edelheer")
    elif choice1 == "doorgang twee":
        print("Een goede keuze voor de avonturier")
    else:
        return "Je bent gestorven aan keuze stress."

    time.sleep(delay)

    print()
    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")
    print()

    time.sleep(delay)
    
    choice4 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

    if choice4 == "tafel":
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