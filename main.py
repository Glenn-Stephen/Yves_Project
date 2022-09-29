import sys
import json

import toutes_les_classes
import fonctions_pour_les_classes


chemin = r"C:\Users\Glenn\Script_Yves\projet_python\Data_base.json"

with open(chemin, "r", encoding='utf-8') as f:
    data_base = json.load(f)

while True:
    choice = ""
    while choice == "":
        choice = input("""
        Bienvenu au sein de notre établissement de formation !

        Que voulez-vous faire ?

        1. Afficher les informations des travailleurs
        2. Ajouter un travailleur
        3. Supprimer un travailleur
        4. Sauvegarder et quitter

        Votre réponse : """)
        choice_number = ["1", "2", "3", "4"]
        if choice not in choice_number:
            print("Veillez choisir une option valide !")
            choice = ""

    if choice == "1":
        fonctions_pour_les_classes.display_data_base(data_base)
    elif choice == "2":
        number = fonctions_pour_les_classes.type_worker()
        fonctions_pour_les_classes.add_worker(number, data_base)
    elif choice == "3":
        fonctions_pour_les_classes.remove_worker(data_base)
    elif choice == "4":
        fonctions_pour_les_classes.save_data_base(chemin, data_base)
        sys.exit()


