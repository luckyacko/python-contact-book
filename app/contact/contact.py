class Contact:
    def __init__(self, name, adress, number) -> None:
        self.name = name
        self.adress = adress
        self.number = number


    def change_name(self, name):
        self.name = name

    def change_adress(self, adress):
        self.adress = adress
    
    def change_number(self, number):
        self.number = number
