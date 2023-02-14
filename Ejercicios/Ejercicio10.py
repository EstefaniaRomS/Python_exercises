class Auto:
    def __init__(self,brand,modelo,año):
        self.brand = brand
        self.modelo = modelo
        self.año = año
        
        def get_brand(self):
            return self.brand
        def setter_brand(self):
            self.brand=brand
            
        def get_modelo(self):
            return self.modelo
        def setter_modelo(self):
            self.modelo=modelo
            
        def get_año(self):
            return self.año
        def setter_año(self):
            self.año=año
            
    def imprimir(self):
        print(f'Marca:{self.brand}, Modelo:{self.modelo}, Año:{self.año}')

brand=str(input("Ingrese la marca:  "))
modelo=str(input("Ingrese el modelo: "))
año=int(input("Digite el año: "))

Auto1 = Auto(brand,modelo,año)
Auto1.imprimir()