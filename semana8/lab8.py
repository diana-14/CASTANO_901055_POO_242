from faker import Faker
fake = Faker()

class Person:
    def __init__(self, dni, name, lastname):
        self.dni = dni
        self.name = name
        self.lastname = lastname

    def __repr__(self):
        return f"person=(DNI={self.dni}, Name={self.name}, lastname={self.lastname})"
    
    #numero de personas que vamos a crear
def generate_people(count):
        people = []
        for _ in range (count):
            dni = fake.ssn()
            name = fake.first_name()
            lastname = fake.last_name()

            person = Person(dni, name, lastname)
            people.append(person)
        return people
    
    #Mostrar el contenido de la lista de personas
def get_people(people_list):
        for person in people_list:
            print(person)

number = int(input("por favor ingrese el numero de personas a agregar:\n"))
array_people = generate_people(number)

get_people(array_people)