class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

    def __repr__(self):
        return f"Coche(marca='{self.marca}', modelo='{self.modelo}', año={self.año})"


mi_coche = Coche("Toyota", "Corolla", 2022)

print(mi_coche)        
print(repr(mi_coche))  
