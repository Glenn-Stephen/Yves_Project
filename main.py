
class Workers:
    def __init__(self):
        print("Bienvenu au sein de notre établissement de formation !")
        print()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.sex = self.get_sex()
        self.birthday = self.get_birthday()
        self.address = self.get_address()

    def get_first_name(self):
        self.first_name = input("Quel est votre nom ? ")
        if self.first_name == "":
            print("Veillez entrer un nom !")
            self.get_first_name()
        return self.first_name.upper()

    def get_last_name(self):
        self.last_name = input("Quel est votre prénom ? ")
        if self.last_name == "":
            print("Veillez entrer un prénom !")
            self.get_last_name()
        return self.last_name.title()

    def get_sex(self):
        self.sex = input("Quel est votre sex (H ou F) ? ")
        if self.sex.upper() != "H" and self.sex.upper() != "F":
            print("Veillez répondre par H ou F !")
            self.get_sex()
        return self.sex.upper()
    
    def get_birthday(self):
        self.birthday = input("Quel est votre date de naissance (DD/MM/YYYY) ? ")
        return self.birthday
            
    def get_address(self):
        self.address = input("Quelle est votre adresse ? ")
        if self.address == "":
            print("Veillez entrer votre adresse actuelle !")
            self.get_address()
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
        matricule
        filière


class Maintenance(Workers):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    worker = Workers()
    worker
    print(worker.first_name, worker.last_name)