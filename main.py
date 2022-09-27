
class Workers:
    """ Classe travailleur """
    def __init__(self):
        """ Constructeur d'un travailleur """
        print("Bienvenu au sein de notre établissement de formation !")
        print()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.date_of_birth = self.get_date_of_birth()
        self.place_of_birth = self.get_place_of_birth()
        self.sex = self.get_sex()
        self.nationality = self.get_nationality()
        self.address = self.get_address()

    def get_first_name(self):
        self.first_name = input("Nom : ")
        return self.first_name.upper()

    def get_last_name(self):
        self.last_name = input("Prénom : ")
        return self.last_name.title()

    def get_date_of_birth(self):
        self.date_of_birth = input("Date de naissance (DD/MM/YYYY) : ")
        return self.date_of_birth

    def get_place_of_birth(self):
        self.place_of_birth = input("Lieu de naissance : ")
        return self.place_of_birth

    def get_sex(self):
        self.sex = input("Sex (H ou F) : ")
        return self.sex.upper()

    def get_nationality(self):
        self.nationality = input("Nationalité : ")
        return self.nationality
            
    def get_address(self):
        self.address = input("Adresse : ")
        return self.address

class Administration(Workers):
    def __init__(self):
        super().__init__()

class Teacher(Workers):
    def __init__(self):
        super().__init__()
        matricule
        profession

class Student(Workers):
    def __init__(self):
        super().__init__()
        self.department = self.get_department()
        self.section = self.get_section()
        self.cycle = self.get_cycle()
        self.level_of_study = self.get_level_of_study()

    def get_department(self):
        self.department = input("Département : ")
        return self.department

    def get_section(self):
        self.section = input("Section : ")
        return self.section

    def get_cycle(self):
        self.cycle = input("Cycle : ")
        return self.cycle

    def get_level_of_study(self):
        self.level_of_study = input("Level of study : ")
        return self.level_of_study


class Maintenance(Workers):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    student = Student()
    student