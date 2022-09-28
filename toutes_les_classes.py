
class Workers:
    def __init__(self):
        print("Bienvenu au sein de notre établissement de formation !")
        print()
        self.information = {}
        self.get_first_name()
        self.get_last_name()
        self.get_date_of_birth()
        self.get_place_of_birth()
        self.get_sex()
        self.get_nationality()
        self.get_address()

    def get_first_name(self):
        self.first_name = input("Nom : ")
        self.information["Nom"] = self.first_name.upper()

    def get_last_name(self):
        self.last_name = input("Prénom : ")
        self.information["Prénom"] = self.last_name.title()

    def get_date_of_birth(self):
        self.date_of_birth = input("Date de naissance (DD/MM/YYYY) : ")
        self.information["Date de naissance"] = self.date_of_birth

    def get_place_of_birth(self):
        self.place_of_birth = input("Lieu de naissance : ")
        self.information["Lieu de naissance"] = self.place_of_birth.capitalize()

    def get_sex(self):
        self.sex = input("Sex (H ou F) : ")
        self.information["Sex"] = self.sex.upper()

    def get_nationality(self):
        self.nationality = input("Nationalité : ")
        self.information["Nationalité"] = self.nationality.capitalize()
            
    def get_address(self):
        self.address = input("Adresse : ")
        self.information["Adresse"] = self.address.title()

    def display_information(self):
        return self.information

class Administration(Workers):
    def __init__(self):
        super().__init__()
        self.get_function()
    
    def get_function(self):
        self.function = input("Fonction : ")
        self.information["Fonction"] = self.function.title()

class Teacher(Workers):
    def __init__(self):
        super().__init__()
        self.get_grade()
        self.get_subject_taught()

    def get_grade(self):
        self.grade = input("Grade : ")
        self.information["Grade"] = self.grade

    def get_subject_taught(self):
        self.subject_taught = input("Matière enseigné : ")
        self.information["Matière enseigné"] = self.subject_taught

class Student(Workers):
    def __init__(self):
        super().__init__()
        self.get_department()
        self.get_section()
        self.get_cycle()
        self.get_level_of_study()

    def get_department(self):
        self.department = input("Département : ")
        self.information["Département"] = self.department.title()

    def get_section(self):
        self.section = input("Section : ")
        self.information["Section"] = self.section.title()

    def get_cycle(self):
        self.cycle = input("Cycle : ")
        self.information["Cycle"] = self.cycle.title()

    def get_level_of_study(self):
        self.level_of_study = input("Niveau d'étude : ")
        self.information["Niveau d'étude"] = self.level_of_study

class Maintenance(Workers):
    def __init__(self):
        super().__init__()
        self.get_occupation()
        self.get_company()

    def get_company(self):
        self.company = input("Société : ")
        self.information["Société"] = self.company

    def get_occupation(self):
        self.occupation = input("Profession : ")
        self.information["Profession"] = self.occupation

