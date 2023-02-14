class colegios:
    def __init__(self,nombre,ciudad,barrio):
        self.nombre = nombre
        self.ciudad = ciudad
        self.barrio = barrio
        
        def get_nombre(self):
            return self.nombre
        def setter_nombre(self):
            self.nombre=nombre
            
        def get_ciudad(self):
            return self.ciudad
        def setter_ciudad(self):
            self.ciudad=ciudad
            
        def get_barrio(self):
            return self.barrio
        def setter_barrio(self):
            self.barrio=barrio
            
    def imprimir(self):
        print("Colegio 1:")
        print(f'Nombre: {self.nombre}, Ciudad: {self.ciudad}, Barrio: {self.barrio}')

nombre=str(input("Ingrese el nombre del colegio:  "))
ciudad=str(input("Ingrese la cuidad donde se encuentra la sede: "))
barrio=str(input("Ingrese el barrio: "))

colegio1 = colegios(nombre,ciudad,barrio)
colegio1.imprimir()