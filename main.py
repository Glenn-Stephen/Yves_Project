
class Workers:
    def __init__(self):
        print("Bienvenu au sein de notre établissement de formation !")
        print()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.old = self.get_old()
        self.address = self.get_address()

    def get_first_name(self):
        self.first_name = input("Quel est votre nom ? ")
        return self.first_name

    def get_last_name(self):
        self.last_name = input("Quel est votre prénom ? ")
        return self.last_name
    
    def get_old(self):
        self.old = input("Quel est votre age ? ")
        if not self.old.isdigit() or int(self.old) >= 100:
            print("Veillez entrer votre age réel !")
            self.get_old()
        return self.old
            
    def get_address(self):
        self.address = input("Quelle est votre adresse ? ")
        return self.address

class Administration(Workers):
    def __init__(self):
        super().__init__()

class Teacher(Workers):
    def __init__(self):
        super().__init__()

class Student(Workers):
    def __init__(self):
        super().__init__()

class Maintenance(Workers):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    worker = Workers()
    worker