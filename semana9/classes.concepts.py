# class person:
#     def __init__(self, name:str, lastname, age:int):
#        self.name = name
#        self.lastname = lastname
#        self.age = age
#        self.ismarriedwith = ismarriedwith = None
#        self.nationality = nationality = None
    
#     def __str__(self):
#         spone_name = self.ismarriedwith.name if self.ismarriedwith else"None"
#         return f"name={self.name}, spouse={spouse_name}"
    
#     #def __repr__(self):
#     #   return f"person(name={self.name}, lastname={self.lastname}, age={self.age}, spouse={self.ismarriedwith}, nationality={self.nationality})"

#     def get_married(self, person: "person"):
#         self.ismarriedwith = person
#         person.ismarriedwith = self


# person_1=person(name="james", lastname="rodriguez", age=33)
# person_2=person(name="luis", lastname="diaz", age=25)
# person_3=person(name="luisa", lastname="perez", age=24)


# person_1.get_married(person_3)
# person_3.get

# print(person_1)

class person:
    def __init__(self, name:str, lastname, age:int):
       self.__name = name
       self.__lastname = lastname
       self.__age = age
     
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self._name = name
    
    def get_lastname(self):
        return self.__lastname

    def set

    def set_age(self, age):
        self.__age = age
    

    
    def __repr__(self):
         return f"name={self._name()}, lastname={self._lastname()}, age={self.__age}"


person_1=person(name="james", lastname="rodriguez", age=33)
person_2=person(name="luis", lastname="diaz", age=25)
person_3=person(name="luisa", lastname="perez", age=24)

person_1.set_name("david")

print(person_1)

