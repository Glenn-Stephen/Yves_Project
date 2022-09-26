
class Workers:
    def __init__(self):
        print("Bienvenu au sein de notre établissement de formation !")
        print()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.address = self.get_address()

    def get_first_name(self):
        self.first_name = input("Quel est votre nom ? ")
        return self.first_name

    def get_last_name(self):
        self.last_name = input("Quel est votre prénom ? ")
        return self.last_name

    def get_address(self):
        self.address = input("Quelle est votre adresse ? ")
        return self.address


if __name__ == "__main__":
    worker = Workers()
    worker