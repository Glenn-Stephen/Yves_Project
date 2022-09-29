import json

import toutes_les_classes


def display_data_base(data_base):
    for a, b in data_base.items():
        print(a, " :", b)


def add_worker(number, data_base):
    matricule = ""
    while matricule == "":
        matricule = input("Créer le matricule du travailleur : ")
        if matricule in data_base:
            print(f"Le matricule {matricule} existe déjà dans la base de données !")
            matricule = ""

    if number == "1":
        worker_administration = toutes_les_classes.Administration()
        worker_administration_infos = worker_administration.display_information()
        data_base[matricule] = worker_administration_infos
    elif number == "2":
        worker_teacher = toutes_les_classes.Teacher()
        worker_teacher_infos = worker_teacher.display_information()
        data_base[matricule] = worker_teacher_infos
    elif number == "3":
        worker_student = toutes_les_classes.Student()
        worker_student_infos = worker_student.display_information()
        data_base[matricule] = worker_student_infos
    elif number == "4":
        worker_maintenance = toutes_les_classes.Maintenance()
        worker_maintenance_infos = worker_maintenance.display_information()
        data_base[matricule] = worker_maintenance_infos
        

def remove_worker(data_base):
    matricule = ""
    while matricule == "":
        matricule = input("Entrer le matricule du travailleur à supprimer : ")
        if matricule not in data_base:
            print(f"Le matricule {matricule} n'existe pas dans la base de données !")
            matricule = ""
            print()
        else:
            del data_base[matricule]
            print(f"Le matricule {matricule} a été supprimé de la base de données.")


def save_data_base(chemin, data_base):
    with open(chemin, "w", encoding='utf-8') as f:
        json.dump(data_base, f, indent=4)
        print("Les données ont bien été sauvergardé.")


def type_worker():
    worker = input("""
    Quel travailleur voulez-vous ajouter ?
    
    1. Administration
    2. Enseignant
    3. Etudiant
    4. Entretien
    
    Votre choix : """)
    liste_worker = ["1", "2", "3", "4"]
    if worker not in liste_worker:
        print("Veillez entrer un numéro correspondant à un travail !")
        type_worker()
    return worker

