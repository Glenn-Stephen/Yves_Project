import json
import sys


class Workers:
    """Cette classe a pour objectif de créer un objet travailleur
    en récupérant dans son constructeur toutes les informations qu'un 
    travailleur peut posséder.
    """
    def __init__(self):
        """Définition du constructeur d'un travailleur"""
        self.information = {}
        self.get_first_name()
        self.get_last_name()
        self.get_date_of_birth()
        self.get_place_of_birth()
        self.get_sex()
        self.get_nationality()
        self.get_address()

    def get_first_name(self):
        """Récupérer le nom du travailleur"""
        self.first_name = input("Nom : ")
        self.information["Nom"] = self.first_name.upper()

    def get_last_name(self):
        """Récupérer le prénom du travailleur"""
        self.last_name = input("Prénom : ")
        self.information["Prénom"] = self.last_name.title()

    def get_date_of_birth(self):
        """Récupérer la date de naissance du travailleur"""
        self.date_of_birth = input("Date de naissance (DD/MM/YYYY) : ")
        self.information["Date de naissance"] = self.date_of_birth

    def get_place_of_birth(self):
        """Récupérer le lieu de naissance du travailleur"""
        self.place_of_birth = input("Lieu de naissance : ")
        self.information["Lieu de naissance"] = self.place_of_birth.capitalize()

    def get_sex(self):
        """Récupérer le genre du travailleur"""
        self.sex = input("Sex (H ou F) : ")
        self.information["Sex"] = self.sex.upper()

    def get_nationality(self):
        """Récupérer la nationalité du travailleur"""
        self.nationality = input("Nationalité : ")
        self.information["Nationalité"] = self.nationality.capitalize()
            
    def get_address(self):
        """Récupérer l'adresse du travailleur"""
        self.address = input("Adresse : ")
        self.information["Adresse"] = self.address.title()

    def display_information(self):
        """Cette méthode permet de récupérer toutes les informations d'un travailleur,
        et de les retourner.
        Returns:
            Dict: Dictionnaire contenant les informations du travailleur
        """
        return self.information

class Administration(Workers):
    """Cette classe crée un travailleur administration en héritant de la classe
    parent travailleurs"""
    def __init__(self):
        """Ce constructeur hérite du constructeur parent"""
        super().__init__()
        self.get_function()
    
    def get_function(self):
        """Récupérer la fonction de l'administrateur"""
        self.function = input("Fonction : ")
        self.information["Fonction"] = self.function.title()

class Teacher(Workers):
    """Cette classe crée un travailleur enseignant en héritant de la classe
    parent travailleurs"""
    def __init__(self):
        """Ce constructeur hérite du constructeur parent"""
        super().__init__()
        self.get_grade()
        self.get_subject_taught()

    def get_grade(self):
        """Récupérer le grade de l'enseignant"""
        self.grade = input("Grade : ")
        self.information["Grade"] = self.grade

    def get_subject_taught(self):
        """Récupérer la matière dispensé par l'enseignant"""
        self.subject_taught = input("Matière enseigné : ")
        self.information["Matière enseigné"] = self.subject_taught

class Student(Workers):
    """Cette classe crée un travailleur étudiant en héritant de la classe
    parent travailleurs"""
    def __init__(self):
        super().__init__()
        """Ce constructeur hérite du constructeur parent"""
        self.get_department()
        self.get_section()
        self.get_cycle()
        self.get_level_of_study()

    def get_department(self):
        """Récupérer le département de l'étudiant"""
        self.department = input("Département : ")
        self.information["Département"] = self.department.title()

    def get_section(self):
        """Récupérer la section de l'étudiant"""
        self.section = input("Section : ")
        self.information["Section"] = self.section.title()

    def get_cycle(self):
        """Récupérer le cycle de l'étudiant"""
        self.cycle = input("Cycle : ")
        self.information["Cycle"] = self.cycle.title()

    def get_level_of_study(self):
        """Récupérer le niveau d'étude de l'étudiant"""
        self.level_of_study = input("Niveau d'étude : ")
        self.information["Niveau d'étude"] = self.level_of_study

class Maintenance(Workers):
    """Cette classe crée un travailleur entretien en héritant de la classe
    parent travailleurs"""
    def __init__(self):
        """Ce constructeur hérite du constructeur parent"""
        super().__init__()
        self.get_occupation()
        self.get_company()

    def get_company(self):
        """Récupérer la société de l'agent"""
        self.company = input("Société : ")
        self.information["Société"] = self.company

    def get_occupation(self):
        """Récupérer le poste de l'agent"""
        self.occupation = input("Profession : ")
        self.information["Profession"] = self.occupation


def display_data_base(data_base):
    """Affiche la base de données contenant toutes les informations,
    de tous les travailleurs toutes classes confondu,
    avec leur matricule et leurs informations personnelles."""
    for a, b in data_base.items():
        print(a, " :", b)


def add_worker(number, data_base):
    """Ajouter les informations d'un nouveau travailleur en lui créant un matricule"""
    matricule = ""
    while matricule == "":
        matricule = input("Créer le matricule du travailleur : ")
        if matricule in data_base:
            print(f"Le matricule {matricule} existe déjà dans la base de données !")
            matricule = ""

    if number == "1":
        worker_administration = Administration()
        worker_administration_infos = worker_administration.display_information()
        data_base[matricule] = worker_administration_infos
    elif number == "2":
        worker_teacher = Teacher()
        worker_teacher_infos = worker_teacher.display_information()
        data_base[matricule] = worker_teacher_infos
    elif number == "3":
        worker_student = Student()
        worker_student_infos = worker_student.display_information()
        data_base[matricule] = worker_student_infos
    elif number == "4":
        worker_maintenance = Maintenance()
        worker_maintenance_infos = worker_maintenance.display_information()
        data_base[matricule] = worker_maintenance_infos
        

def remove_worker(data_base):
    """Supprimer les informations d'un travailleur à partir de son matricule"""
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
    """Sauvegarder les informations des travailleurs dans la base de données"""
    with open(chemin, "w", encoding='utf-8') as f:
        json.dump(data_base, f, indent=4)
        print("Les données ont bien été sauvergardé.")


def type_worker():
    """Sélectionner le type de travailleur à partir du numéro correspondant"""
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


if __name__ == "__main__":
    """Cette condition permet de ne pas exécuter le script lorsque le fichier
    est importer comme module pour utiliser l'une de ces classes ou fonctions"""

    # Cette variable doit contenir le chemin vers la base de données
    chemin = r"C:\Users\Glenn\Script_Yves\projet_python\Data_base.json"

    # Lecture des informations contenu dans la base de données
    with open(chemin, "r", encoding='utf-8') as f:
        data_base = json.load(f)

    print("Bienvenu au sein de notre établissement de formation !")

    # Script
    while True:
        choice = ""
        while choice == "":
            choice = input("""
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
            display_data_base(data_base)
        elif choice == "2":
            number = type_worker()
            add_worker(number, data_base)
        elif choice == "3":
            remove_worker(data_base)
        elif choice == "4":
            save_data_base(chemin, data_base)
            sys.exit()
