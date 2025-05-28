class People:
    def __init__(self, name):
        self.name = name

 # setter for name
    @property
    def name(self):
        return self._name

    #setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name

class Student(People):
    def __init__(self, name, house):

        super().__init__(name)
        self.house = house

    @classmethod
    def get(cls):

        name = input("name: ")
        house = input("house: ")
        return cls(name, house)



    def __str__(self):
        return f"{self.name} is from {self.house}"





    # setter function
    @property
    def house(self):
        return self._house

    # getter function
    @house.setter
    def house(self, house):
        if house not in ["isc", "vnc"]:
            raise ValueError("invalid house")
        self._house = house




def main():
    stud = Student.get()
    print(stud)




main()
