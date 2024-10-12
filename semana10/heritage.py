#clase abstracta
class person:
    def __init__(self, dni, name, lastname, age):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.age = age

class Student(person):
    def __init__(self, dni, name, lastname, age, code):
        super(). __init__(dni, name, lastname, age)
        self.code = code
        self.subjects = []

    
    def add_subject(self, subject):
        self.__subjects.append(subject)


    def __str__(self):
        return f"Nombre: {self.name}, codigo: {self.code}, asignatras: {self.subjects}"

class Professor(person):
    def __init__(self, dni, name, lastname, age, device, desktop):
        super(). __init__(dni, name, lastname, age)
        self.device = device
        self.desktop = desktop

Student_1 = Student(1234, "luis", "soto", 21, 12233)
Student_1.add_subject("Matematicas")
Professor_1 = Professor(1234, "luis", "soto", 21, "laptop", 16)

print(Student_1)
print(Professor_1)

